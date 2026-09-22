# Component catalog

To add or change anything, find its row here. The "cookbook phrase" is what a module
asks for; the home is the folder; the contract is the shape it must satisfy.

All homes are paths from the base (`sunrise-v1`). App code is under `apps/support-agent/`.

| Cookbook phrase | Home | Contract | Register in | Test in |
| --- | --- | --- | --- | --- |
| add a data model | apps/support-agent/src/domain/models.py | Pydantic BaseModel | dataModel.md | apps/support-agent/tests/domain |
| add a data generator | apps/support-agent/src/data/ | writes to data/generated | pipelines.md | apps/support-agent/tests/data |
| add a loader or parser | apps/support-agent/src/ingest/ | load(src) -> text or Doc | pipelines.md | apps/support-agent/tests/ingest |
| add a chunker | apps/support-agent/src/index/ | split(text) -> list[Chunk] | pipelines.md | apps/support-agent/tests/index |
| add an index | apps/support-agent/src/index/ | build(); search(q, k) | pipelines.md | apps/support-agent/tests/index |
| add a store adapter | apps/support-agent/src/adapters/ | wraps an external store | registry.md | apps/support-agent/tests/adapters |
| add a retrieval pipeline component | apps/support-agent/src/rag/ | search / rerank / answer | registry.md | apps/support-agent/tests/rag |
| add a prompt | apps/support-agent/src/prompts/ | template string or builder | registry.md | n/a |
| add a tool | apps/support-agent/src/tools/ | Tool schema + handler(args) | registry.md | apps/support-agent/tests/tools |
| add an MCP server | apps/support-agent/src/tools/*_mcp.py | FastMCP exposing tools | registry.md | manual |
| add an agent | apps/support-agent/src/agents/ | run(input, ctx) -> Decision | registry.md | apps/support-agent/tests/agents |
| add an orchestrator | apps/support-agent/src/agents/orchestrator.py | route or loop agents + tools | registry.md | apps/support-agent/tests/agents |
| add a memory component | apps/support-agent/src/memory/ | read / write context | registry.md | apps/support-agent/tests/memory |
| add a guardrail component | apps/support-agent/src/guardrails/ | check(payload) -> GuardResult | registry.md | apps/support-agent/tests/guardrails |
| add an eval metric | data/eval/metrics/ | score(case, output) -> float | harness.md | apps/support-agent/tests/eval |
| extend the golden set | data/eval/golden.json | list[EvalCase] | harness.md | n/a |
| add an observability component | apps/support-agent/src/observability/ | trace / measure | registry.md | apps/support-agent/tests/observability |
| add an API route | apps/support-agent/src/serving/api/ | FastAPI route | interfaces.md | apps/support-agent/tests/serving |
| add a UI view | apps/support-agent/src/serving/ui/ | Streamlit page | interfaces.md | manual |
| add a CLI command | apps/support-agent/src/app/ | subcommand of the sunrise CLI | interfaces.md | apps/support-agent/tests/app |
| add a config | apps/support-agent/src/config/ | typed settings | registry.md | n/a |
| add a report | apps/support-agent/reports/ | generated md or html | registry.md | n/a |

A kind of thing not listed here is added to this table first (record why in decisions.md), then built.
