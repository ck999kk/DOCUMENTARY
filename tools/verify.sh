#!/usr/bin/env bash
set -euo pipefail

# DOCUMENTARY manifest verify/update utility
# - Verifies SHA256 integrity against VERIFICATION/integrity_manifest.sha256
# - Regenerates the manifest (excluding volatile and internal paths)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
MANIFEST_REL="VERIFICATION/integrity_manifest.sha256"
MANIFEST_PATH="$REPO_ROOT/$MANIFEST_REL"

usage() {
  cat <<EOF
Usage:
  tools/verify.sh check          Verify files against manifest
  tools/verify.sh update         Regenerate manifest and verify
  tools/verify.sh help           Show this help

Notes:
  - Runs from repository root: $REPO_ROOT
  - Excludes: .git/, .venv/, .DS_Store, and the manifest itself
EOF
}

ensure_hasher() {
  if command -v shasum >/dev/null 2>&1; then
    HASH_CMD=(shasum -a 256)
    VERIFY_CMD=(shasum -a 256 -c "$MANIFEST_REL")
  elif command -v sha256sum >/dev/null 2>&1; then
    HASH_CMD=(sha256sum)
    VERIFY_CMD=(sha256sum -c "$MANIFEST_REL")
  else
    echo "Error: neither 'shasum' nor 'sha256sum' found on PATH" >&2
    exit 2
  fi
}

regen_manifest() {
  echo "[verify.sh] Regenerating manifest at $MANIFEST_REL"
  cd "$REPO_ROOT"
  # Backup existing manifest if present
  if [ -f "$MANIFEST_PATH" ]; then
    cp -p "$MANIFEST_PATH" "${MANIFEST_PATH}.bak.$(date +%Y%m%d-%H%M%S)" || true
  fi
  # Build list and hash. Exclude volatile/internal paths.
  find . -type f \
    -not -name '.DS_Store' \
    -not -path './.git/*' \
    -not -path './.venv/*' \
    -not -path "./$MANIFEST_REL" \
    -not -path './VERIFICATION/integrity_manifest.sha256.bak*' \
    -print0 \
    | xargs -0 "${HASH_CMD[@]}" \
    > "$MANIFEST_REL"
}

verify_manifest() {
  echo "[verify.sh] Verifying manifest $MANIFEST_REL from repo root"
  cd "$REPO_ROOT"
  # Show only failures; summarize count and set exit code accordingly
  if command -v rg >/dev/null 2>&1; then
    FAILS=$("${VERIFY_CMD[@]}" 2>/dev/null | rg -n 'FAILED' | tee /dev/stderr | wc -l | tr -d ' ')
  else
    FAILS=$("${VERIFY_CMD[@]}" 2>/dev/null | grep -n 'FAILED' | tee /dev/stderr | wc -l | tr -d ' ')
  fi
  if [ "$FAILS" -eq 0 ]; then
    echo "[verify.sh] Integrity OK (0 failures)"
  else
    echo "[verify.sh] Integrity FAILED ($FAILS failures)" >&2
    return 1
  fi
}

main() {
  local cmd=${1:-check}
  case "$cmd" in
    help|-h|--help)
      usage; exit 0 ;;
    check|verify)
      ensure_hasher
      verify_manifest ;;
    update|regen|rebuild)
      ensure_hasher
      regen_manifest
      verify_manifest ;;
    *)
      echo "Unknown command: $cmd" >&2
      usage
      exit 2 ;;
  esac
}

main "$@"

