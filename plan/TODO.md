# PTO-ISA MCP Server — Implementation Plan & TODO

## Status: v0.1.0 — Core Implementation Complete

All 13 MCP tools are implemented and tested against real documentation.

---

## Completed

- [x] Project scaffolding (pyproject.toml, directory structure)
- [x] `models.py` — Pydantic data models (InstructionInfo, ScalarOp, ControlFlowOp, AuxiliaryOp, ISAStore, etc.)
- [x] `loader.py` — Parse all markdown/manifest at startup (ISA pages, assembly family docs, scalar/CF/aux ops, grammar)
- [x] `tools.py` — 13 MCP tool definitions with annotations (readOnly, idempotent)
- [x] `server.py` — FastMCP server setup + transport config
- [x] `__main__.py` — CLI entry point (argparse: docs_path, --host, --port, --stdio, --log-level)
- [x] `repo_manager.py` — Auto-clone/pull pto-isa from gitcode.com when no docs_path provided
- [x] `test_loader.py` — 28 tests against real docs (all passing)
- [x] `README.md` — Usage documentation

## Future Enhancements

- [ ] Add `comm/` category to assembly family docs mapping (currently comm instructions load from ISA pages but have no family doc)
- [ ] Add tool: `get_instruction_raw` — return only the raw markdown for an instruction (lighter weight)
- [ ] Add tool: `get_comm_ops` — dedicated tool for communication instructions (TBROADCAST, TREDUCE, etc.)
- [ ] Add integration tests that spin up the MCP server and issue real tool calls
- [ ] Add caching headers / ETag support for HTTP transport
- [ ] Add `--watch` mode that reloads docs on file changes
- [ ] Package and publish to PyPI
- [ ] Add Dockerfile for containerized deployment
- [ ] Support filtering scalar ops by return type or operand count
- [ ] Add full-text search across scalar/CF/aux ops (not just ISA instructions)

## Architecture Decisions

1. **Dynamic loading**: All docs are parsed at startup into an in-memory ISAStore. No lazy loading. This keeps tool calls fast and stateless.
2. **JSON manifest**: `manifest.yaml` is actually JSON. Loader tries `json.loads()` first with YAML fallback.
3. **Assembly enrichment**: If an instruction's ISA page has no assembly forms, the loader fills them from the assembly family docs.
4. **Error handling**: Tools return actionable error dicts with suggestions (similar names, hints to use list_* tools).
5. **No env vars**: `docs_path` is a CLI positional argument (now optional), not an env var.
6. **Auto-clone**: When no `docs_path` is given, the server clones `https://gitcode.com/cann/pto-isa` into `~/.cache/npu-coding-mcp/` and pulls on every startup to stay current.
