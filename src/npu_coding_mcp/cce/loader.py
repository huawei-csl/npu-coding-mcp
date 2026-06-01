"""Load and query the CCE documentation index."""

import re
import sqlite3
from pathlib import Path
from typing import Optional

from npu_coding_mcp.cce.models import ChapterInfo, SearchResult, SectionContent, SectionInfo


class CCEStore:
    """Access layer for the CCE documentation index."""

    def __init__(self, docs_path: Path, index_path: Path):
        self.docs_path = docs_path.resolve()
        self.index_path = index_path.resolve()
        self.conn = sqlite3.connect(str(self.index_path))
        self.conn.row_factory = sqlite3.Row

    def close(self):
        self.conn.close()

    @staticmethod
    def _s(row, key, default=""):
        val = row[key]
        return val if val is not None else default

    # ── Search ──────────────────────────────────────────────

    def search(self, query: str, max_results: int = 10) -> list[SearchResult]:
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
        parent = str(Path(file_path).parent) + "/"
        if parent == "./":
            return 0
        prefix = str(Path(file_path).parent) + "/" + Path(file_path).stem + "/"
        row = self.conn.execute(
            "SELECT COUNT(*) FROM sections WHERE file_path LIKE ? AND file_path != ?",
            (prefix + "%", file_path),
        ).fetchone()
        return row[0] if row else 0

    def list_chapters(self) -> list[ChapterInfo]:
        chapters = []
        seen_dirs = set()

        chapter_titles = {
            "01_简介": "简介",
            "02_异构编程环境配置与编译器使用": "异构编程环境配置与编译器使用",
            "03_CCEIntrinsic介绍": "CCE Intrinsic介绍",
            "04_CCEIntrinsic特性": "CCE Intrinsic特性",
            "05_CCEIntrinsic样例": "CCE Intrinsic样例",
            "06_API参考": "API参考",
        }

        chapter_map = {
            "01_简介": "Introduction — overview of CCE Intrinsic and supported hardware platforms",
            "02_异构编程环境配置与编译器使用": "Environment Setup — BiSheng compiler installation, configuration, and quick compilation example",
            "03_CCEIntrinsic介绍": "CCE Intrinsic Introduction — heterogeneous programming model, kernel functions, SPMD parallel model, multi-pipeline async",
            "04_CCEIntrinsic特性": "CCE Intrinsic Features — execution space qualifiers, address space qualifiers, predefined macros, global variables, scalars",
            "05_CCEIntrinsic样例": "CCE Intrinsic Examples — Vector, Cube, and Mix operator examples with host/device code",
            "06_API参考": "API Reference — vector computation, matrix computation, data movement, synchronization APIs",
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


def load_store(docs_path: Path, index_path: Path) -> CCEStore:
    if not index_path.exists():
        raise FileNotFoundError(f"Index not found at {index_path}. Run 'build-cce-index' first.")
    return CCEStore(docs_path, index_path)
