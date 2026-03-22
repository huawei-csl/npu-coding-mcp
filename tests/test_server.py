"""Basic tests for the npu-coding-mcp server."""

import pytest
from fastmcp import Client

from npu_coding_mcp.server import mcp


@pytest.fixture
def client():
    return Client(mcp)


@pytest.mark.asyncio
async def test_list_tools(client):
    async with client:
        tools = await client.list_tools()
    tool_names = {t.name for t in tools}
    assert "generate_tiling_struct" in tool_names
    assert "explain_ascendc_error" in tool_names
    assert "scaffold_custom_op" in tool_names


@pytest.mark.asyncio
async def test_list_resources(client):
    async with client:
        resources = await client.list_resources()
    uris = {str(r.uri) for r in resources}
    assert "ascend://docs/memory-hierarchy" in uris
    assert "ascend://docs/tiling-guide" in uris
    assert "ascend://docs/ascendc-primer" in uris


@pytest.mark.asyncio
async def test_list_prompts(client):
    async with client:
        prompts = await client.list_prompts()
    prompt_names = {p.name for p in prompts}
    assert "kernel_review_prompt" in prompt_names
    assert "op_design_prompt" in prompt_names


@pytest.mark.asyncio
async def test_generate_tiling_struct(client):
    async with client:
        result = await client.call_tool(
            "generate_tiling_struct",
            {
                "fields": [
                    {"name": "tileLength", "type": "uint32_t"},
                    {"name": "totalLength", "type": "uint32_t"},
                ],
                "struct_name": "MyTiling",
            },
        )
    text = result.content[0].text
    assert "MyTiling" in text
    assert "tileLength" in text
    assert "uint32_t" in text


@pytest.mark.asyncio
async def test_generate_tiling_struct_invalid_type(client):
    async with client:
        with pytest.raises(Exception):
            await client.call_tool(
                "generate_tiling_struct",
                {
                    "fields": [{"name": "x", "type": "double"}],
                },
            )


@pytest.mark.asyncio
async def test_explain_ascendc_error_known(client):
    async with client:
        result = await client.call_tool(
            "explain_ascendc_error",
            {"error_message": "tensor alignment error at offset 0x100"},
        )
    assert "alignment" in result.content[0].text.lower()


@pytest.mark.asyncio
async def test_explain_ascendc_error_unknown(client):
    async with client:
        result = await client.call_tool(
            "explain_ascendc_error",
            {"error_message": "some totally unknown error xyz"},
        )
    assert "No automatic match" in result.content[0].text


@pytest.mark.asyncio
async def test_scaffold_custom_op(client):
    async with client:
        result = await client.call_tool(
            "scaffold_custom_op",
            {
                "op_name": "MyAddOp",
                "input_dtypes": ["float16", "float16"],
                "output_dtypes": ["float16"],
                "op_type": "Elewise",
            },
        )
    text = result.content[0].text
    assert "myadd" in text.lower() or "MyAddOp" in text
    assert "float16" in text or "half" in text


@pytest.mark.asyncio
async def test_scaffold_custom_op_invalid_type(client):
    async with client:
        with pytest.raises(Exception):
            await client.call_tool(
                "scaffold_custom_op",
                {
                    "op_name": "BadOp",
                    "input_dtypes": ["float16"],
                    "output_dtypes": ["float16"],
                    "op_type": "InvalidType",
                },
            )
