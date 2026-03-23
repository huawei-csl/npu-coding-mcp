"""Basic tests for the npu-coding-mcp server."""

import pytest
from fastmcp import Client

from npu_coding_mcp import mcp


@pytest.fixture
def client():
    return Client(mcp)


@pytest.mark.asyncio
async def test_list_tools(client):
    async with client:
        tools = await client.list_tools()
    tool_names = {t.name for t in tools}
    assert "compile_pto_isa_kernel" in tool_names


@pytest.mark.asyncio
async def test_list_resources(client):
    async with client:
        resources = await client.list_resources()
    uris = {str(r.uri) for r in resources}
    assert "ascend://docs/memory-hierarchy" in uris


@pytest.mark.asyncio
async def test_list_prompts(client):
    async with client:
        prompts = await client.list_prompts()
    prompt_names = {p.name for p in prompts}
    assert "kernel_review_prompt" in prompt_names
    assert "op_design_prompt" in prompt_names
