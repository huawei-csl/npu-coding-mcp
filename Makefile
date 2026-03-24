.PHONY: install install-local build test

install:
	uv sync --group dev

install-local:
	uv pip install -e .

build:
	uv build

lint:
	uv run ruff check . 

test:
	uv run pytest

run:
	uv run npu-coding-mcp
