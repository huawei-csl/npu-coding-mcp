"""Basic tests for the npu-coding-mcp server."""

import pytest
from fastmcp import Client

from npu_coding_mcp import mcp
from npu_coding_mcp.tools import parse_tool_result, CompilationResult


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
async def test_mcp_tool_pto_isa_kernel_simple_matmul(client):
    kernel_source = "https://raw.githubusercontent.com/huawei-csl/pto-kernels/refs/heads/main/csrc/kernel/kernel_simple_matmul.cpp"

    async with client:
        result = await client.call_tool("compile_pto_isa_kernel", {"kernel_source": kernel_source})

    assert result is not None
    compile_result: CompilationResult = parse_tool_result(result)
    assert compile_result.success == True


@pytest.mark.asyncio
async def test_mcp_tool_pto_isa_kernel_abs(client):
    kernel_source = "https://raw.githubusercontent.com/huawei-csl/pto-kernels/refs/heads/main/csrc/kernel/kernel_abs.cpp"

    async with client:
        result = await client.call_tool("compile_pto_isa_kernel", {"kernel_source": kernel_source})

    assert result is not None
    compile_result: CompilationResult = parse_tool_result(result)
    assert compile_result.success == False # this fails!



@pytest.mark.asyncio
async def test_mcp_tool_pto_isa_kernel_batch_matrix_square(client):
    kernel_source = "https://raw.githubusercontent.com/huawei-csl/pto-kernels/refs/heads/main/csrc/kernel/kernel_batch_matrix_square.cpp"

    async with client:
        result = await client.call_tool("compile_pto_isa_kernel", {"kernel_source": kernel_source})

    assert result is not None
    compile_result: CompilationResult = parse_tool_result(result)
    assert compile_result.success == True



@pytest.mark.asyncio
async def test_mcp_tool_pto_isa_kernel_fast_hadamard(client):
    kernel_source = "https://raw.githubusercontent.com/huawei-csl/pto-kernels/refs/heads/main/examples/jit_cpp/fast_hadamard/standard/fast_hadamard.cpp"

    async with client:
        result = await client.call_tool("compile_pto_isa_kernel", {"kernel_source": kernel_source, "define_membase": True})

    assert result is not None
    compile_result: CompilationResult = parse_tool_result(result)
    assert compile_result.success == True


"""
@pytest.mark.asyncio
async def test_mcp_tool_pto_isa_kernel_tri_inv_col_sweep(client):
    kernel_source = "https://raw.githubusercontent.com/huawei-csl/pto-kernels/refs/heads/main/csrc/kernel/kernel_tri_inv_col_sweep.cpp"

    async with client:
        result = await client.call_tool("compile_pto_isa_kernel", {"kernel_source": kernel_source})

    assert result is not None
    compile_result: CompilationResult = parse_tool_result(result)
    assert compile_result.success == True



@pytest.mark.asyncio
async def test_mcp_tool_pto_isa_kernel_tri_inv_rec_unroll(client):
    kernel_source = "https://raw.githubusercontent.com/huawei-csl/pto-kernels/refs/heads/main/csrc/kernel/kernel_tri_inv_rec_unroll.cpp"

    async with client:
        result = await client.call_tool("compile_pto_isa_kernel", {"kernel_source": kernel_source})

    assert result is not None
    print(Result)
    assert False


@pytest.mark.asyncio
async def test_mcp_tool_pto_isa_kernel_tri_inv_trick(client):
    kernel_source = "https://raw.githubusercontent.com/huawei-csl/pto-kernels/refs/heads/main/csrc/kernel/kernel_tri_inv_trick.cpp"

    async with client:
        result = await client.call_tool("compile_pto_isa_kernel", {"kernel_source": kernel_source})

    assert result is not None
    print(Result)
    assert False

"""