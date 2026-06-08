"""Split the monolithic CCE-9.0.0.md into per-section files under data/cce_docs/.

Mirrors the AscendC docs layout: numbered directories, per-section .md files with
metadata headers (Section, PDF Pages), and a 00-index.md TOC.

Usage:
    python scripts/split_cce_docs.py /home/ebezati/CCE-9.0.0.md data/cce_docs/
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SECTION_HEADING_RE = re.compile(r"^## (\d+(?:\.\d+)*)\s+(.+)$")
BOILERPLATE_RE = re.compile(r"^## (功能说明|接口原型|参数说明|流水类型)\s*$")
PIPE_BOUNDARY_RE = re.compile(r"^PIPE\\?_?[VS]\s*$")

CHAPTER_TITLES: dict[str, str] = {
    "1": "简介",
    "2": "异构编程环境配置与编译器使用",
    "3": "CCE Intrinsic介绍",
    "4": "CCE Intrinsic特性",
    "5": "CCE Intrinsic样例",
    "6": "API参考",
}


def _section_to_dirname(section_number: str, title: str) -> str:
    parts = section_number.split(".")
    padded = "_".join(f"{int(p):02d}" for p in parts)
    short_title = title.replace("/", "_").replace("&amp;", "&").replace(" ", "")
    short_title = short_title[:40]
    return f"{padded}_{short_title}"


def _section_to_filename(section_number: str, title: str) -> str:
    return _section_to_dirname(section_number, title) + ".md"


def _fix_merged_content(entries: list[dict]) -> list[dict]:
    """Fix Docling merging bug: when two consecutive API sections have content
    merged into the second one, split it back.

    Pattern: section A has only boilerplate sub-headings, section B has
    both A's and B's actual content. The boundary is identified by PIPE_V/S lines.

    Skips sections that are parent containers (their number is a prefix of
    the next section's number), as they naturally have no direct content.
    """
    fixed: list[dict] = []
    i = 0
    while i < len(entries):
        entry = entries[i]
        body = entry["content_lines"]
        meaningful = [ln for ln in body if ln.strip() and not BOILERPLATE_RE.match(ln.strip())]

        # Skip parent containers — they naturally have no content
        is_container = False
        if i + 1 < len(entries):
            next_sec = entries[i + 1]["section_number"]
            cur_sec = entry["section_number"]
            if next_sec.startswith(cur_sec + "."):
                is_container = True

        if len(meaningful) >= 2 or i + 1 >= len(entries) or is_container:
            fixed.append(entry)
            i += 1
            continue

        next_entry = entries[i + 1]
        next_body = next_entry["content_lines"]
        next_meaningful = [ln for ln in next_body if ln.strip() and not BOILERPLATE_RE.match(ln.strip())]

        if len(next_meaningful) <= 2:
            fixed.append(entry)
            i += 1
            continue

        # Find all PIPE lines and check if content precedes the first PIPE
        pipe_indices: list[int] = []
        has_content_before_first_pipe = False
        for j, line in enumerate(next_body):
            if PIPE_BOUNDARY_RE.match(line.strip()):
                pipe_indices.append(j)
                if not has_content_before_first_pipe and len(pipe_indices) == 1:
                    # Check if there's text content before this PIPE (past boilerplate)
                    for k in range(j):
                        if (
                            next_body[k].strip()
                            and not BOILERPLATE_RE.match(next_body[k].strip())
                            and "PIPE" not in next_body[k].strip()
                        ):
                            has_content_before_first_pipe = True
                            break

        if not pipe_indices:
            fixed.append(entry)
            i += 1
            continue

        # Choose split point based on whether content precedes the first PIPE
        if has_content_before_first_pipe and len(pipe_indices) >= 1:
            split_at = pipe_indices[0]
        elif len(pipe_indices) >= 2:
            split_at = pipe_indices[1]
        else:
            fixed.append(entry)
            i += 1
            continue

        entry["content_lines"] = entry["content_lines"] + next_body[: split_at + 1]
        next_entry["content_lines"] = next_body[split_at + 1 :]
        fixed.append(entry)
        fixed.append(next_entry)
        i += 2

    return fixed


def split_docs(input_path: Path, output_dir: Path) -> int:
    """Split the monolithic markdown into per-section files.

    Returns the number of section files created.
    """
    text = input_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    sections: list[tuple[int, str, str]] = []
    for i, line in enumerate(lines):
        m = SECTION_HEADING_RE.match(line)
        if m:
            sections.append((i, m.group(1), m.group(2)))

    if not sections:
        print("Error: no numbered section headings found")
        sys.exit(1)

    end_line = len(lines)
    for i, line in enumerate(lines):
        if line.startswith("## Extracted Images"):
            end_line = i
            break

    section_entries: list[dict] = []
    for idx, (line_num, sec_num, title) in enumerate(sections):
        if line_num >= end_line:
            break
        next_line = sections[idx + 1][0] if idx + 1 < len(sections) else end_line
        body = lines[line_num + 1 : next_line]
        section_entries.append(
            {
                "section_number": sec_num,
                "title": title,
                "content_lines": body,
            }
        )

    # Fix Docling merging bug
    section_entries = _fix_merged_content(section_entries)

    sec_title_lookup: dict[str, str] = {e["section_number"]: e["title"] for e in section_entries}

    # Build TOC with links
    toc_content = "# CCE Intrinsic 开发指南 — 目录\n\n"
    toc_content += "> **Source**: CCE-9.0.0.pdf (140 pages)\n\n"
    for e in section_entries:
        sec_num = e["section_number"]
        title = e["title"]
        indent = "  " * (sec_num.count("."))
        chapter_num = sec_num.split(".")[0]
        chapter_dir = _section_to_dirname(chapter_num, CHAPTER_TITLES.get(chapter_num, f"Chapter{chapter_num}"))
        if "." not in sec_num:
            link = f"{chapter_dir}/{_section_to_filename(sec_num, title)}"
        else:
            parent_num = sec_num.rsplit(".", 1)[0]
            parent_title = sec_title_lookup.get(parent_num, "")
            filename = _section_to_filename(sec_num, title)
            if parent_title:
                parent_dir = _section_to_dirname(parent_num, parent_title)
                link = f"{chapter_dir}/{parent_dir}/{filename}"
            else:
                link = f"{chapter_dir}/{filename}"
        toc_content += f"{indent}- [{sec_num} {title}]({link})\n"

    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "00-index.md").write_text(toc_content, encoding="utf-8")

    # Copy images into output dir if source images exist
    _copy_images(input_path, output_dir)

    count = 0
    for entry in section_entries:
        sec_num = entry["section_number"]
        title = entry["title"]
        body_lines = entry["content_lines"]

        chapter_num = sec_num.split(".")[0]
        chapter_dir_name = _section_to_dirname(chapter_num, CHAPTER_TITLES.get(chapter_num, f"Chapter{chapter_num}"))
        chapter_dir = output_dir / chapter_dir_name

        if "." not in sec_num:
            section_dir = chapter_dir
        else:
            parent_num = sec_num.rsplit(".", 1)[0]
            parent_title = sec_title_lookup.get(parent_num, "")
            if parent_title:
                parent_dirname = _section_to_dirname(parent_num, parent_title)
                section_dir = chapter_dir / parent_dirname
            else:
                section_dir = chapter_dir

        section_dir.mkdir(parents=True, exist_ok=True)
        filename = _section_to_filename(sec_num, title)
        filepath = section_dir / filename

        md_content = f"# {title}\n\n"
        md_content += f"> **Section**: {sec_num}\n\n"
        body_text = "\n".join(body_lines)

        # Fix image paths: images/ -> ../images/ depending on section depth
        depth = len(section_dir.relative_to(output_dir).parts)
        prefix = "../" * depth + "images/"
        body_text = body_text.replace("](images/", f"]({prefix}")

        md_content += body_text

        filepath.write_text(md_content, encoding="utf-8")
        count += 1

    _remove_empty_dirs(output_dir)

    print(f"Created {count} section files in {output_dir}")
    print(f"TOC written to {output_dir / '00-index.md'}")
    return count


def _remove_empty_dirs(root: Path) -> None:
    for d in sorted(root.rglob("*"), key=lambda p: len(str(p)), reverse=True):
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()


def _copy_images(input_md: Path, output_dir: Path) -> None:
    """Copy extracted images from the input markdown's sibling images/ dir
    into output_dir/images/, if they exist."""
    images_src = input_md.parent / "images"
    images_dst = output_dir / "images"
    if images_src.is_dir() and not images_dst.exists():
        images_dst.mkdir(parents=True, exist_ok=True)
        count = 0
        for img in images_src.iterdir():
            if img.is_file():
                (images_dst / img.name).write_bytes(img.read_bytes())
                count += 1
        if count:
            print(f"Copied {count} images to {images_dst}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Split CCE markdown into per-section files")
    parser.add_argument("input", type=Path, help="Path to CCE-9.0.0.md")
    parser.add_argument(
        "output", type=Path, nargs="?", default=Path("data/cce_docs"), help="Output directory (default: data/cce_docs)"
    )
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: input file not found: {args.input}")
        sys.exit(1)

    _ = split_docs(args.input, args.output.resolve())
    return 0


if __name__ == "__main__":
    main()
