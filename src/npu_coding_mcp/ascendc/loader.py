"""Load and query the AscendC documentation index."""

import re
import sqlite3
from pathlib import Path
from typing import Optional

from npu_coding_mcp.ascendc.models import ChapterInfo, SearchResult, SectionContent, SectionInfo


class AscendCStore:
    """Access layer for the AscendC documentation index."""

    def __init__(self, docs_path: Path, index_path: Path):
        self.docs_path = docs_path.resolve()
        self.index_path = index_path.resolve()
        self.conn = sqlite3.connect(str(self.index_path))
        self.conn.row_factory = sqlite3.Row

    def close(self):
        self.conn.close()

    @staticmethod
    def _s(row, key, default=""):
        """Safely get a string value from a row."""
        val = row[key]
        return val if val is not None else default

    # ── Search ──────────────────────────────────────────────

    def search(self, query: str, max_results: int = 10) -> list[SearchResult]:
        """Full-text search across all documentation sections."""
        escaped = query.replace('"', '""')
        sql = """SELECT file_path, section_title, section_number, pdf_pages,
                        snippet(sections, 2, '<mark>', '</mark>', '...', 40) AS snippet,
                        bm25(sections, 0.0, 10.0, 5.0, 0.0, 0.0) AS rank
                 FROM sections
                 WHERE sections MATCH ?
                 ORDER BY rank
                 LIMIT ?"""
        results = []
        try:
            for row in self.conn.execute(sql, (f'"{escaped}"', max_results)):
                results.append(
                    SearchResult(
                        title=self._s(row, "section_title"),
                        path=self._s(row, "file_path"),
                        section_number=self._s(row, "section_number"),
                        pdf_pages=self._s(row, "pdf_pages"),
                        snippet=self._s(row, "snippet"),
                        rank=round(row["rank"], 2) if row["rank"] else 0.0,
                    )
                )
        except sqlite3.OperationalError:
            # Fallback: try without quoting for single-word queries
            try:
                for row in self.conn.execute(sql, (escaped, max_results)):
                    results.append(
                        SearchResult(
                            title=self._s(row, "section_title"),
                            path=self._s(row, "file_path"),
                            section_number=self._s(row, "section_number"),
                            pdf_pages=self._s(row, "pdf_pages"),
                            snippet=self._s(row, "snippet"),
                            rank=round(row["rank"], 2) if row["rank"] else 0.0,
                        )
                    )
            except sqlite3.OperationalError:
                pass

        return results

    def search_api(self, api_name: str) -> list[SearchResult]:
        """Search for an API name in the API reference section only."""
        escaped = api_name.replace('"', '""')
        sql = """SELECT file_path, section_title, section_number, pdf_pages,
                        snippet(sections, 2, '<mark>', '</mark>', '...', 40) AS snippet
                 FROM sections
                 WHERE sections MATCH ?
                   AND file_path LIKE '06_API参考/%'
                 ORDER BY rank
                 LIMIT 10"""
        results = []
        try:
            for row in self.conn.execute(sql, (f'"{escaped}"',)):
                results.append(
                    SearchResult(
                        title=self._s(row, "section_title"),
                        path=self._s(row, "file_path"),
                        section_number=self._s(row, "section_number") or "",
                        pdf_pages=self._s(row, "pdf_pages") or "",
                        snippet=self._s(row, "snippet") or "",
                    )
                )
        except sqlite3.OperationalError:
            pass
        return results

    # ── Content reading ─────────────────────────────────────

    def get_section(self, path: str) -> Optional[SectionContent]:
        """Read a single section by its relative path."""
        md_file = self.docs_path / path
        if not md_file.exists():
            return None

        content = md_file.read_text(encoding="utf-8")

        title = ""
        section_number = ""
        pdf_pages = ""

        m = re.search(r"^# (.+)$", content, re.MULTILINE)
        if m:
            title = m.group(1).strip()
        m = re.search(r"> \*\*Section\*\*:\s*(\S+)", content)
        if m:
            section_number = m.group(1).strip()
        m = re.search(r"> \*\*PDF Pages\*\*:\s*(\S+)", content)
        if m:
            pdf_pages = m.group(1).strip()

        return SectionContent(
            title=title,
            path=path,
            section_number=section_number,
            pdf_pages=pdf_pages,
            content=content,
        )

    def list_sections(self, parent_path: Optional[str] = None) -> list[SectionInfo]:
        """List all sections under a parent path, or all chapters."""
        if parent_path:
            prefix = parent_path.rstrip("/") + "/"
            sql = """SELECT file_path, section_title, section_number, pdf_pages
                     FROM sections
                     WHERE file_path LIKE ?
                     ORDER BY file_path"""
            rows = self.conn.execute(sql, (prefix + "%",)).fetchall()
        else:
            sql = """SELECT file_path, section_title, section_number, pdf_pages
                     FROM sections
                     ORDER BY file_path"""
            rows = self.conn.execute(sql).fetchall()

        results = []
        for row in rows:
            # Count subsections: files deeper than this one
            sub_count = self._count_subsections(self._s(row, "file_path"))
            results.append(
                SectionInfo(
                    title=self._s(row, "section_title"),
                    path=self._s(row, "file_path"),
                    pdf_pages=self._s(row, "pdf_pages") or "",
                    section_number=self._s(row, "section_number") or "",
                    subsection_count=sub_count,
                )
            )
        return results

    def _count_subsections(self, file_path: str) -> int:
        """Count how many sections are nested deeper than this one (not siblings)."""
        parent = str(Path(file_path).parent) + "/"
        if parent == "./":
            return 0
        # Files that are deeper than this entry
        prefix = str(Path(file_path).parent) + "/" + Path(file_path).stem + "/"
        row = self.conn.execute(
            "SELECT COUNT(*) FROM sections WHERE file_path LIKE ? AND file_path != ?",
            (prefix + "%", file_path),
        ).fetchone()
        return row[0] if row else 0

    def list_chapters(self) -> list[ChapterInfo]:
        """List top-level chapters with description."""
        chapters = []
        seen_dirs = set()

        chapter_titles = {
            "01_入门教程": "入门教程",
            "02_编程指南": "编程指南",
            "03_算子实践参考": "算子实践参考",
            "04_兼容性迁移指南": "兼容性迁移指南",
            "05_可视化专区": "可视化专区",
            "06_API参考": "API参考",
            "目_录": "目录",
        }

        chapter_map = {
            "01_入门教程": "Getting Started — AscendC introduction, environment setup, quick start tutorials (SIMD and SIMT)",
            "02_编程指南": "Programming Guide — programming models (SIMD, SIMT, AI CPU), compilation, APIs, hardware, debugging, compatibility",
            "03_算子实践参考": "Operator Practice — SIMD/SIMT operator implementation patterns, performance optimization, debugging",
            "04_兼容性迁移指南": "Migration Guide — compatibility notes and 351x architecture migration guidance",
            "05_可视化专区": "Visualization — visual development tools and debugging aids",
            "06_API参考": "API Reference — complete SIMD API, SIMT API, Utils API, AI CPU API documentation (1,561 sections)",
            "目_录": "Table of Contents — document outline and navigation",
        }

        rows = self.conn.execute("SELECT file_path, section_title FROM sections ORDER BY file_path").fetchall()
        for row in rows:
            fp = self._s(row, "file_path")
            top_dir = fp.split("/")[0]
            if top_dir in seen_dirs:
                continue
            seen_dirs.add(top_dir)

            count_row = self.conn.execute(
                "SELECT COUNT(*) FROM sections WHERE file_path LIKE ?",
                (top_dir + "/%",),
            ).fetchone()
            count = count_row[0] if count_row else 0

            chapters.append(
                ChapterInfo(
                    title=chapter_titles.get(top_dir, top_dir),
                    path=top_dir + "/",
                    section_count=count,
                    description=chapter_map.get(top_dir, ""),
                )
            )

        return chapters

    def get_chapter_tree(self, chapter_path: str) -> list[SectionInfo]:
        """Get the section tree for a chapter, organized by hierarchy."""
        prefix = chapter_path.rstrip("/") + "/"
        rows = self.conn.execute(
            """SELECT file_path, section_title, section_number, pdf_pages
               FROM sections WHERE file_path LIKE ?
               ORDER BY file_path""",
            (prefix + "%",),
        ).fetchall()

        results = []
        for row in rows:
            results.append(
                SectionInfo(
                    title=self._s(row, "section_title"),
                    path=self._s(row, "file_path"),
                    pdf_pages=self._s(row, "pdf_pages") or "",
                    section_number=self._s(row, "section_number") or "",
                    subsection_count=self._count_subsections(self._s(row, "file_path")),
                )
            )
        return results


def load_store(docs_path: Path, index_path: Path) -> AscendCStore:
    """Create an AscendCStore from a docs directory and index."""
    if not index_path.exists():
        raise FileNotFoundError(
            f"Index not found at {index_path}. Run 'ascendc-mcp build-index {docs_path} {index_path}' first."
        )
    return AscendCStore(docs_path, index_path)
