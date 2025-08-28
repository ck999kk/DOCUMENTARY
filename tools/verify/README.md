# verify

CLI for generating and checking the SHA256 integrity manifest used by DOCUMENTARY.

Examples

- Generate manifest for common evidence types:
  ```bash
  python -m venv .venv && source .venv/bin/activate
  pip install -e .
  verify generate --root .. --output ../VERIFICATION/integrity_manifest.sha256
  ```

- Check an existing manifest:
  ```bash
  verify check ../VERIFICATION/integrity_manifest.sha256 --root ..
  ```

- Advanced include/exclude with globs (relative to `--root`):
  ```bash
  verify generate --root .. \
    --output ../VERIFICATION/integrity_manifest.sha256 \
    -I "Combined_Attachments/**" -X "**/*.tmp.txt" -X "**/drafts/**"
  ```
