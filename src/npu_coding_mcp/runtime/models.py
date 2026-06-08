"""Pydantic data models for Runtime MCP server."""

from pydantic import BaseModel


class ChapterInfo(BaseModel):
    title: str
    path: str
    section_count: int = 0
    description: str = ""


class SectionInfo(BaseModel):
    title: str
    path: str
    pdf_pages: str = ""
    section_number: str = ""
    subsection_count: int = 0


class SearchResult(BaseModel):
    title: str
    path: str
    section_number: str = ""
    pdf_pages: str = ""
    snippet: str = ""
    rank: float = 0.0


class SectionContent(BaseModel):
    title: str
    path: str
    section_number: str = ""
    pdf_pages: str = ""
    content: str
