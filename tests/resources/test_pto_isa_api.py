"""Basic tests for the npu-coding-mcp resources."""

import pytest
from fastmcp import Client

from npu_coding_mcp import mcp


@pytest.fixture
def client():
    return Client(mcp)


@pytest.mark.asyncio
async def test_list_resources(client):
    async with client:
        resources = await client.list_resources()
    uris = {str(r.uri) for r in resources}
    assert "ascend://docs/memory-hierarchy" in uris