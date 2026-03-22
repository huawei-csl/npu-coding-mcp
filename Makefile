.PHONY: install install-local build test

install:
	uv sync --group dev

install-local:
	uv pip install -e .

build:
	uv build

test:
	uv run pytest
