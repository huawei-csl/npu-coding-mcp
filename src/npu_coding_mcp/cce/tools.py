"""MCP tool definitions for CCE documentation server."""

from fastmcp import FastMCP

from npu_coding_mcp.cce.loader import CCEStore

TRANSLATION_PREFIX = (
    "\n\n> **Language note:** The documentation below is in Chinese. "
    "Translate it to English in your response, but keep all code blocks, "
    "API names, type signatures, and technical identifiers unchanged.\n\n"
)

TOOL_ANNOTATIONS = {
    "readOnlyHint": True,
    "idempotentHint": True,
    "destructiveHint": False,
    "openWorldHint": False,
}


def _apply_language(content: str, language: str) -> str:
    if language == "zh":
        return content
    return TRANSLATION_PREFIX + content


def register_tools(mcp: FastMCP, store: CCEStore) -> None:
    """Register all MCP tools on the FastMCP server."""

    @mcp.tool(annotations=TOOL_ANNOTATIONS)
    def cce_search_docs(
        query: str,
        max_results: int = 10,
        language: str = "en",
    ) -> dict:
        """Full-text search across all CCE Intrinsic documentation sections.

        Content is in Chinese. Use language="en" (default) for translation instructions,
        or language="zh" for raw Chinese.

        Args:
            query: Search query string (supports SQLite FTS5 syntax)
            max_results: Maximum number of results (1-50)
            language: "en" for English translation instruction, "zh" for raw Chinese
        """
        max_results = max(1, min(50, max_results))
        results = store.search(query, max_results)

        return {
            "query": query,
            "language": language,
            "total_matches": len(results),
            "results": [
                {
                    "title": r.title,
                    "path": r.path,
                    "section_number": r.section_number,
                    "pdf_pages": r.pdf_pages,
                    "snippet": r.snippet,
                    "relevance": r.rank,
                }
                for r in results
            ],
        }

    @mcp.tool(annotations=TOOL_ANNOTATIONS)
    def cce_get_section(
        path: str,
        language: str = "en",
    ) -> dict:
        """Read a specific CCE documentation section by its file path.

        The path is relative to the docs root (e.g., '06_API参考/06_03_04_双目运算/06_03_04_01_vadd_vsub_vmul_vdiv.md').
        Set language="zh" to receive raw Chinese content.

        Args:
            path: Relative file path to the section markdown file
            language: "en" for English translation instruction, "zh" for raw Chinese
        """
        section = store.get_section(path)
        if section is None:
            return {
                "error": f"Section not found: {path}",
                "hint": "Use cce_search_docs() or cce_get_chapter_tree() to find valid paths.",
            }

        content = section.content
        content = _apply_language(content, language)

        return {
            "title": section.title,
            "path": section.path,
            "section_number": section.section_number,
            "pdf_pages": section.pdf_pages,
            "content": content,
        }

    @mcp.tool(annotations=TOOL_ANNOTATIONS)
    def cce_list_chapters() -> dict:
        """List all top-level chapters in the CCE Intrinsic documentation.

        Returns chapter titles, paths, section counts, and descriptions.
        Use this as a starting point to understand what topics are available.
        """
        chapters = store.list_chapters()
        return {
            "total_chapters": len(chapters),
            "chapters": [
                {
                    "title": ch.title,
                    "path": ch.path,
                    "section_count": ch.section_count,
                    "description": ch.description,
                }
                for ch in chapters
            ],
        }

    @mcp.tool(annotations=TOOL_ANNOTATIONS)
    def cce_get_chapter_tree(chapter_path: str) -> dict:
        """Get the full section hierarchy for a specific CCE chapter.

        Returns all sections and subsections under the given chapter path, with
        their section numbers and subsection counts.

        Args:
            chapter_path: Chapter directory path (e.g., '06_API参考/' or '06_API参考/06_03_向量计算接口/')
        """
        sections = store.get_chapter_tree(chapter_path)
        if not sections:
            if not chapter_path.endswith("/"):
                sections = store.get_chapter_tree(chapter_path + "/")

        return {
            "chapter_path": chapter_path,
            "total_sections": len(sections),
            "sections": [
                {
                    "title": s.title,
                    "path": s.path,
                    "section_number": s.section_number,
                    "pdf_pages": s.pdf_pages,
                    "subsection_count": s.subsection_count,
                }
                for s in sections
            ],
        }

    @mcp.tool(annotations=TOOL_ANNOTATIONS)
    def cce_search_api(api_name: str) -> dict:
        """Search for an API function in the CCE API Reference chapter.

        Fast targeted lookup — searches only 06_API参考/ for function/type/macro names.
        Use this instead of cce_search_docs() when you know the exact API name.

        Args:
            api_name: API function, type, or macro name (e.g., 'vadd', 'mad', 'copy_gm_to_ubuf')
        """
        results = store.search_api(api_name)
        return {
            "query": api_name,
            "total_matches": len(results),
            "results": [
                {
                    "title": r.title,
                    "path": r.path,
                    "section_number": r.section_number,
                    "pdf_pages": r.pdf_pages,
                    "snippet": r.snippet,
                }
                for r in results
            ],
        }

    @mcp.tool(annotations=TOOL_ANNOTATIONS)
    def cce_get_toc() -> dict:
        """Get the complete CCE document table of contents.

        Returns the full TOC from the index file (00-index.md), including links to all sections.
        Use this to understand the overall document structure.
        """
        toc_file = store.docs_path / "00-index.md"
        if not toc_file.exists():
            return {"error": "TOC index file not found"}

        content = toc_file.read_text(encoding="utf-8")

        return {
            "source": "00-index.md",
            "toc": content,
        }
