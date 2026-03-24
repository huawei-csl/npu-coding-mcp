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

test-resources:
	uv run pytest -v tests/resources

test-tools:
	uv run pytest -v tests/tools

run:
	uv run npu-coding-mcp
