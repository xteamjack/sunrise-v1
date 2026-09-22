# Architecture (frozen)

This is a monorepo. The base is `sunrise-v1`; apps live under apps/ and this app is
apps/support-agent. Shared data lives under data/, memory under _memory/, docs under docs/.
The solution is built in planes; each plane has a folder home inside the app. New code
goes in the home named by its component type (see componentCatalog.md). Change a plane or
a home only with a decision in decisions.md.

## Planes and homes (paths from the base)
- Domain (data models)                      apps/support-agent/src/domain
- Data pipeline (generate, load, parse)     apps/support-agent/src/data, apps/support-agent/src/ingest
- Index (vector, keyword)                   apps/support-agent/src/index
- Adapters (orders DB, vector store, cache) apps/support-agent/src/adapters
- Retrieval (retrieve, rerank, ground)      apps/support-agent/src/rag
- Prompts                                   apps/support-agent/src/prompts
- Agents (support, triage, specialists)     apps/support-agent/src/agents
- Tools (and MCP servers)                   apps/support-agent/src/tools
- Memory (session, long-term)               apps/support-agent/src/memory
- Guardrails (input, output)                apps/support-agent/src/guardrails
- Observability (tracing, cost)             apps/support-agent/src/observability
- Interface (API, UI, CLI)                  apps/support-agent/src/serving, apps/support-agent/src/app
- Config                                    apps/support-agent/src/config
- Reports                                   apps/support-agent/reports
- Shared data (knowledge, generated, orders db)  data/knowledge, data/generated
- Eval (metrics, golden set, gate)          data/eval

## The flow
data -> index -> retrieval (rag) -> agents (+ tools, + memory) -> serving,
with guardrails around every request, eval gating every change, observability always on.

## The canon (frozen facts)
Order SE-4021; Refund Policy v4 Section 2 (full refund if claimed within 15 days of a
late delivery); refunds above Rs 5,000 need human approval; simple warranty is support,
disputes go to Legal. Stack: Claude Sonnet/Haiku, Voyage, Qdrant, Redis, Claude Agent
SDK, MCP/FastMCP, Pydantic, promptfoo, Langfuse, FastAPI, Streamlit, UV. Data stays in Bharat.

## Build order
M3 bootstrap app, M4 data, M5 vectors, M6 RAG, M7 agent core, M8 memory, M9 triage,
M10 eval gate, M11 guardrails, M12 observability, M13 serving, M14 deploy, M15 operate.

## Frozen vs forming
- Frozen: the planes, the homes, the contracts in componentCatalog.md, and the canon.
- Forming: the concrete components (registry.md) and the tuning choices.

## Current state
- Module 1: skeleton. Module 2: Claude Code + this memory. Module 3: bootstrap app (sunrise CLI). Next: Module 4 (data).
