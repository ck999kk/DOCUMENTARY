# Repository Guidelines

## Project Structure & Module Organization
- Evidence first: do not alter originals. Derivatives (OCR, exports) live in existing folders and must be referenced in `LEGAL_DOCUMENTATION/`.
- Key folders: `LEGAL_DOCUMENTATION/` (chain of custody, indices), `VERIFICATION/` (SHA256 manifest), `All_Case_Parties_EML/`, `Combined_Attachments/`, `Additional_Documents/`, `tools/` (scripts/automation).
- Add new automation under `tools/<tool-name>/src`; tests in `tools/<tool-name>/tests`; assets in `tools/<tool-name>/assets`.

## Build, Test, and Development Commands
- Integrity check:
  ```bash
  cd VERIFICATION && sha256sum -c integrity_manifest.sha256
  ```
- Python tools (if present):
  ```bash
  python -m venv .venv && source .venv/bin/activate
  pip install -e tools/<tool-name>
  pytest -q tools/<tool-name>
  ```
- Node.js tools (if present): `npm ci && npm test` in that tool’s folder.

## Coding Style & Naming Conventions
- Preserve evidence filenames; always record SHA256 and commit-pinned URLs.
- Python: 4-space indent; `black` + `isort` for formatting; `ruff`/`flake8` for linting. Use `snake_case` for files/functions/vars; classes in `CapWords`.
- JS/TS: 2-space indent; `eslint` + `prettier`. Filenames in `kebab-case`.

## Testing Guidelines
- Tests live in `tools/<tool-name>/tests/` as `test_*.py` or `*.spec.ts`.
- Aim ≥80% coverage for tools; include an integration test (e.g., verifying a small sample manifest).
- Run `pytest -q` (Python) or `npm test` (Node) before PRs.

## Commit & Pull Request Guidelines
- Conventional Commits: `feat:`, `fix:`, `chore:`, `docs:`, `test:`. Example: `feat(tools/verify): add SHA256 manifest checker`.
- One logical change per PR; include what/why, linked issues, and sample output if adding scripts.
- Update `README.md`, `LEGAL_DOCUMENTATION/` indices, and `VERIFICATION/` manifests when evidence or verification changes.

## Security & Configuration Tips
- Never commit secrets. Provide `.env.example` for any tool requiring config.
- Validate inputs; avoid logging personal data. Always cite commit-pinned URLs and include SHA256 for evidence references.

