"""Build SQLite FTS5 search index from docs/cn/ markdown files."""

import re
import sqlite3
import sys
from pathlib import Path


def parse_section_header(content: str) -> dict:
    """Extract title, section number, and pdf pages from a markdown file header."""
    info = {"title": "", "section_number": "", "pdf_pages": ""}

    # First H1 heading
    m = re.search(r"^# (.+)$", content, re.MULTILINE)
    if m:
        info["title"] = m.group(1).strip()

    # Section number: > **Section**: 1.3.3.1
    m = re.search(r"> \*\*Section\*\*:\s*(\S+)", content)
    if m:
        info["section_number"] = m.group(1).strip()

    # PDF pages: > **PDF Pages**: 70–75
    m = re.search(r"> \*\*PDF Pages\*\*:\s*(\S+)", content)
    if m:
        info["pdf_pages"] = m.group(1).strip()

    # Fallback: use filename stem as title
    if not info["title"]:
        info["title"] = ""
    if not info["section_number"]:
        info["section_number"] = ""

    return info


def build_index(docs_path: Path, index_path: Path) -> int:
    """Build FTS5 index from markdown files. Returns count of indexed documents."""
    docs_path = docs_path.resolve()
    index_path = index_path.resolve()

    index_path.parent.mkdir(parents=True, exist_ok=True)

    # Remove existing index
    if index_path.exists():
        index_path.unlink()

    conn = sqlite3.connect(str(index_path))
    conn.execute("PRAGMA journal_mode=WAL")

    # Content + FTS index in one table
    conn.execute(
        """CREATE VIRTUAL TABLE sections USING fts5(
            file_path,
            section_title,
            section_number,
            pdf_pages,
            content,
            tokenize='unicode61'
        )"""
    )

    count = 0
    for md_file in sorted(docs_path.rglob("*.md")):
        if md_file.name == "00-index.md":
            continue

        rel_path = md_file.relative_to(docs_path)
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        info = parse_section_header(content)

        conn.execute(
            "INSERT INTO sections(file_path, section_title, section_number, pdf_pages, content) VALUES (?, ?, ?, ?, ?)",
            (str(rel_path), info["title"], info["section_number"], info["pdf_pages"], content),
        )
        count += 1

    conn.commit()
    conn.close()

    return count


def main():
    if len(sys.argv) < 3:
        print("Usage: index_builder.py <docs_dir> <index_path>")
        sys.exit(1)

    docs = Path(sys.argv[1])
    output = Path(sys.argv[2])

    if not docs.exists():
        print(f"Error: docs directory not found: {docs}")
        sys.exit(1)

    count = build_index(docs, output)
    size_mb = output.stat().st_size / (1024 * 1024)
    print(f"Index built: {count} documents → {output} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
