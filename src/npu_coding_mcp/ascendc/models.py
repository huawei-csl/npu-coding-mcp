"""Pydantic data models for AscendC MCP server."""

from pydantic import BaseModel


class ChapterInfo(BaseModel):
    """Top-level chapter summary."""

    title: str
    path: str
    section_count: int = 0
    description: str = ""


class SectionInfo(BaseModel):
    """A section within the documentation hierarchy."""

    title: str
    path: str
    pdf_pages: str = ""  # "55-57"
    section_number: str = ""  # "1.3.3.1"
    subsection_count: int = 0


class TocNode(BaseModel):
    """A node in the table of contents tree."""

    title: str
    path: str
    section_number: str = ""
    page: int = 0  # PDF page
    level: int = 0
    children: list["TocNode"] = []

    model_config = {"arbitrary_types_allowed": True}


class SearchResult(BaseModel):
    """A single full-text search result."""

    title: str
    path: str
    section_number: str = ""
    pdf_pages: str = ""
    snippet: str = ""  # FTS5 snippet with match highlighting
    rank: float = 0.0  # bm25 score


class SearchResponse(BaseModel):
    """Response from search_docs tool."""

    query: str
    total_matches: int
    results: list[SearchResult]


class SectionContent(BaseModel):
    """Content of a single documentation section."""

    title: str
    path: str
    section_number: str = ""
    pdf_pages: str = ""
    content: str  # raw markdown
