"""Basic tests for the MCP resources."""

import pytest
from fastmcp import Client

from npu_coding_mcp import mcp


@pytest.fixture
def client():
    return Client(mcp)


@pytest.mark.xfail(reason="Fails when there are no NPUs or npu-smi is not working.", strict=False)
@pytest.mark.asyncio
async def test_npu_smi_info(client):
    async with client:
        result = await client.read_resource("host://npu-smi/info")

    assert result is not None


@pytest.mark.xfail(reason="Fails when Ascend drivers are not installed.", strict=False)
@pytest.mark.asyncio
async def test_npu_driver_version(client):

    async with client:
        result = await client.read_resource("host://npu/driver-version")

    assert result is not None
    assert result[0].text.startswith("version=")

