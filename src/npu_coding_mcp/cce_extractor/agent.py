"""CCE intrinsic extraction via compiler preprocessing.

Compiles individual NPU header files with g++ -E, extracts CCE intrinsic
calls via regex, and captures code snippets around each intrinsic.
"""

from __future__ import annotations

import json
import logging
import os
import re
import subprocess
import tempfile
from pathlib import Path

from openai import OpenAI

from .models import CCEIntrinsicCall

logger = logging.getLogger(__name__)

DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
DEFAULT_MODEL = "deepseek-v4-pro"

GXX = os.environ.get("GXX", "g++")

INTRINSIC_PATTERNS = [
    r"__cce_\w+",
    r"v(adds|subs|muls|divs|maxs|mins|add|sub|mul|div|max|min|abs|cmp|cmps|sel|mov|cvt|sort|and|or|xor|shr|shl|conv|relu|ln|exp|sin|cos|sqrt|rsqrt|rcp|not|sel)",
    r"copy_gm_to_\w+",
    r"copy_ubuf_to_\w+",
    r"copy_\w+_to_\w+",
    r"vec_\w+",
    r"pipe_barrier",
    r"set_mov_pad_val",
    r"set_fmatrix",
    r"set_img2col",
    r"load_cbuf_to_\w+",
    r"vtrc\b",
    r"vcvt\b",
    r"\bmad\b",  # matrix multiply-accumulate (TMATMUL, etc.)
]

_CCE_RE = re.compile(r"\b(" + "|".join(INTRINSIC_PATTERNS) + r")\s*\(", re.IGNORECASE)

_HEADER_WRAPPER = """// wrapper for {name}
#define PTO_NPU_ARCH_{arch_define}
#include <cstdint>
typedef unsigned short half;
typedef unsigned short bfloat16_t;
#define PTO_INTERNAL
#define PTO_INST
#define PTO_ASSERT(...)
#define static_assert(...)
#define __ubuf__
#define __cbuf__
#define __gm__
#define __out__
#define __in__
#define __cce_get_tile_ptr(x) __cce_get_tile_ptr(x)
#define RecordEvent int
#define __tf__
#define BLOCK_BYTE_SIZE 32
#define REPEAT_BYTE 128
#define C0_SIZE_BYTE 512
#define SHIFT_BLOCK_BYTE 5
#define FRACTAL_NZ_ROW 16
#include "{header_path}"
"""


def resolve_api_key(cli_key: str | None = None) -> str:
    if cli_key:
        return cli_key
    env_key = os.environ.get("DEEPSEEK_API_KEY")
    if env_key:
        return env_key
    config_path = Path.home() / ".config" / "npu-coding-mcp" / "deepseek_key"
    if config_path.exists():
        return config_path.read_text().strip()
    raise RuntimeError("DeepSeek API key not found.")


def _get_arch_define(backend: str) -> str:
    return "A2A3" if backend == "a2a3" else "A5"


def _match_balanced_parens(source: str, start: int) -> int | None:
    if start >= len(source) or source[start] != "(":
        return None
    depth = 1
    i = start + 1
    while i < len(source) and depth > 0:
        if source[i] == "(":
            depth += 1
        elif source[i] == ")":
            depth -= 1
        i += 1
    return i if depth == 0 else None


def _extract_intrinsics(text: str) -> list[CCEIntrinsicCall]:
    found: dict[str, str] = {}
    for m in _CCE_RE.finditer(text):
        name = m.group(1)
        paren_pos = m.end() - 1
        sig = name
        if paren_pos < len(text) and text[paren_pos] == "(":
            end = _match_balanced_parens(text, paren_pos)
            if end is not None:
                sig = text[m.start() : end]
        found.setdefault(name.lower(), (name, sig))
    unique = sorted(found.values(), key=lambda x: x[0].lower())
    return [CCEIntrinsicCall(name=n, signature=s) for n, s in unique]


def _extract_code_snippets(text: str, instrs: list[CCEIntrinsicCall]) -> str:
    """Extract code windows around each intrinsic call.

    For each intrinsic, takes 50 lines of context around its occurrence.
    Merges overlapping windows and caps at 50000 bytes.
    """
    lines = text.splitlines()
    match_lines: set[int] = set()
    # Find lines containing intrinsic calls
    for ic in instrs:
        sig_prefix = ic.signature.split("(")[0].strip()
        for i, line in enumerate(lines):
            if sig_prefix in line and "(" in line:
                for offset in range(max(0, i - 100), min(len(lines), i + 101)):
                    match_lines.add(offset)

    # Also capture BinInstr / Op::BinInstr calls (these expand to intrinsics)
    for i, line in enumerate(lines):
        if "BinInstr" in line and "(" in line:
            for offset in range(max(0, i - 100), min(len(lines), i + 101)):
                match_lines.add(offset)

    if not match_lines:
        return ""

    idxs = sorted(match_lines)
    blocks: list[list[int]] = []
    current: list[int] = []

    for i in idxs:
        if current and i <= current[-1] + 3:
            current.append(i)
        else:
            if current:
                blocks.append(current)
            current = [i]
    if current:
        blocks.append(current)

    result_lines: list[str] = []
    for block in blocks:
        start = max(0, block[0] - 2)
        end = min(len(lines), block[-1] + 1)
        result_lines.append(f"// snippet lines {start + 1}-{end}")
        result_lines.extend(lines[start:end])
        result_lines.append("")

    result = "\n".join(result_lines)
    if len(result) > 80000:
        result = result[:80000] + "\n// ... truncated ..."
    return result


def _add_contexts_llm(name: str, instrs: list[CCEIntrinsicCall], api_key: str, model: str) -> None:
    if not instrs:
        return
    items = []
    for i, c in enumerate(instrs):
        items.append(f"  {i + 1}. {c.name}: {c.signature}\n")
    prompt = f"""PTO instruction "{name}" calls these CCE intrinsics:
{"".join(items)}
Give each a one-line context. JSON: {{"contexts": [{{"id": 1, "context": "..."}}]}}"""
    client = OpenAI(api_key=api_key, base_url=DEEPSEEK_BASE_URL)
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=2048,
        )
        content = (resp.choices[0].message.content or "{}").strip()
        if content.startswith("```"):
            content = re.sub(r"^```\w*\n?", "", content)
            content = re.sub(r"\n?```$", "", content)
        data = json.loads(content)
        for item in data.get("contexts", []):
            idx = item.get("id", 0) - 1
            ctx = item.get("context", "")
            if 0 <= idx < len(instrs) and ctx:
                instrs[idx].context = ctx
    except Exception as exc:
        logger.debug("LLM context for %s: %s", name, exc)


def extract_intrinsics(
    header_path: str,
    name: str,
    backend: str,
    include_dir: str,
    api_key: str | None = None,
    model: str = DEFAULT_MODEL,
) -> tuple[list[CCEIntrinsicCall], str]:
    """Extract CCE intrinsics and code snippets from an NPU header."""
    arch = _get_arch_define(backend)
    source = _HEADER_WRAPPER.format(name=name, arch_define=arch, header_path=header_path)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".cpp", delete=False) as f:
        f.write(source)
        tmp = f.name

    try:
        result = subprocess.run(
            [GXX, "-E", "-std=c++17", "-I", include_dir, "-w", tmp],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if not result.stdout or len(result.stdout) < 500:
            return [], ""

        instrs = _extract_intrinsics(result.stdout)
        raw_code = _extract_code_snippets(result.stdout, instrs)

        if api_key and instrs:
            try:
                _add_contexts_llm(name, instrs, api_key, model)
            except Exception:
                pass

        return instrs, raw_code
    except Exception:
        return [], ""
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass
