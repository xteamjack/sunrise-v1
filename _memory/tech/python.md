# Python conventions (any Python app here)

## Platform and version (standard, do not vary)
- Platform: Ubuntu Linux. Windows users work inside WSL (Ubuntu); keep the project in the Linux home, not under /mnt/c or /mnt/d.
- Python: pinned to 3.12 in `apps/support-agent/.python-version`, installed and managed by UV. Do not use another version; version drift is a top source of errors.

## Monorepo and environment
- The base is the `sunrise-v1` folder; run everything from there. Apps live under apps/.
- UV manages each app. Run the app scoped from the base: `uv run --project apps/support-agent ...`.
- Add dependencies with `uv add --project apps/support-agent`; never edit the lockfile by hand.

## Layout
- Application code under apps/<app>/src/, one folder per architecture plane (see solution/architecture.md).
- Tests under apps/<app>/tests/, mirroring the src/ planes.
- Shared data under data/ at the base; memory and docs under _memory/ and docs/.

## Style
- Type hints on public functions. Pydantic for data shapes.
- Format and lint with ruff. Keep functions small and pure where possible.

## Config and secrets
- Settings live in apps/<app>/src/config; read secrets from environment variables (.env at the base), never hard-coded.

## Logging and errors
- Log at the boundaries (tool calls, retrieval, generation). Fail loudly in generation and validation.
