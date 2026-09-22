# Project memory

Long-term memory for the Sunrise agent build, in three layers. Read before
non-trivial work; keep current as the project grows. CLAUDE.md points here.

## generic (any application)
- guidelines.md   naming, house rules, dos and donts, the eight qualities
- workflow.md     how we work: plan, build small, validate, gate, update memory, commit
- (added when needed) glossary.md

## tech (any Python application)
- python.md       project layout, typing, lint and format, tests, logging, config, secrets

## solution (this agentic solution)
- architecture.md      the frozen architecture: planes and their folder homes
- componentCatalog.md  the vocabulary: each component type -> home, contract, register, test
- dataModel.md         the domain models
- registry.md          the live list of concrete components (grows as we build)
- (added by their modules) pipelines.md, agents.md, harness.md, interfaces.md, decisions.md

## The one rule
To add or change anything, find its component type in solution/componentCatalog.md.
It gives the home, the contract, and where to register and test. Never invent a
path. A new kind of thing is added to the catalog first (a decision), then built.
