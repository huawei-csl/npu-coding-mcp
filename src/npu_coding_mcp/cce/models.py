"""Pydantic data models for CCE MCP server."""

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
    pdf_pages: str = ""
    section_number: str = ""
    subsection_count: int = 0


class TocNode(BaseModel):
    """A node in the table of contents tree."""

    title: str
    path: str
    section_number: str = ""
    page: int = 0
    level: int = 0
    children: list["TocNode"] = []

    model_config = {"arbitrary_types_allowed": True}


class SearchResult(BaseModel):
    """A single full-text search result."""

    title: str
    path: str
    section_number: str = ""
    pdf_pages: str = ""
    snippet: str = ""
    rank: float = 0.0


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
    content: str
