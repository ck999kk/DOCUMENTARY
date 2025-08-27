from __future__ import annotations

import argparse
import fnmatch
import hashlib
import os
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


DEFAULT_OUTPUT = "VERIFICATION/integrity_manifest.sha256"
DEFAULT_INCLUDE_EXT = {
    ".pdf",
    ".eml",
    ".msg",
    ".tif",
    ".tiff",
    ".png",
    ".jpg",
    ".jpeg",
    ".txt",
    ".html",
    ".htm",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
}
EXCLUDE_DIRS = {".git", ".github", "__pycache__", "node_modules"}


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest(manifest_path: Path) -> List[Tuple[str, str]]:
    pairs: List[Tuple[str, str]] = []
    with open(manifest_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            sha, rel_path = parts[0], parts[-1]
            pairs.append((sha, rel_path))
    return pairs


def _matches_any(path_str: str, patterns: Iterable[str]) -> bool:
    for pat in patterns:
        if fnmatch.fnmatch(path_str, pat):
            return True
    return False


def iter_files(
    root: Path,
    include_ext: Iterable[str],
    include_globs: Iterable[str] | None = None,
    exclude_globs: Iterable[str] | None = None,
) -> Iterable[Path]:
    include = {e.lower() for e in include_ext}
    include_globs = list(include_globs or [])
    exclude_globs = list(exclude_globs or [])
    for dirpath, dirnames, filenames in os.walk(root):
        # prune excluded dirs
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for name in filenames:
            p = Path(dirpath) / name
            if p.suffix.lower() not in include:
                continue
            rel = p.relative_to(root).as_posix()
            if include_globs and not _matches_any(rel, include_globs):
                continue
            if exclude_globs and _matches_any(rel, exclude_globs):
                continue
            yield p


def generate_manifest(
    root: Path,
    output: Path,
    include_ext: Iterable[str] = DEFAULT_INCLUDE_EXT,
    *,
    include_globs: Iterable[str] | None = None,
    exclude_globs: Iterable[str] | None = None,
) -> List[Tuple[str, str]]:
    root = root.resolve()
    output = output.resolve()
    entries: List[Tuple[str, str]] = []
    for fpath in iter_files(
        root,
        include_ext,
        include_globs=include_globs,
        exclude_globs=exclude_globs,
    ):
        # skip the output manifest itself if within root
        if fpath.resolve() == output:
            continue
        rel = fpath.relative_to(root).as_posix()
        sha = sha256_file(fpath)
        entries.append((sha, rel))
    entries.sort(key=lambda x: x[1])
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w", encoding="utf-8") as f:
        for sha, rel in entries:
            f.write(f"{sha}  {rel}\n")
    return entries


def check_manifest(manifest_path: Path, root: Path) -> Tuple[int, List[str]]:
    root = root.resolve()
    entries = load_manifest(manifest_path)
    errors: List[str] = []
    for expected_sha, rel_path in entries:
        fpath = (root / rel_path).resolve()
        if not fpath.exists():
            errors.append(f"MISSING: {rel_path}")
            continue
        actual_sha = sha256_file(fpath)
        if actual_sha != expected_sha:
            errors.append(
                f"MISMATCH: {rel_path} expected {expected_sha[:16]} got {actual_sha[:16]}"
            )
    return (0 if not errors else 1, errors)


def _parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="verify", description="Integrity manifest tools")
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("generate", help="Generate a SHA256 manifest")
    g.add_argument("--root", default=".", help="Project root (default: .)")
    g.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help=f"Output manifest path (default: {DEFAULT_OUTPUT})",
    )
    g.add_argument(
        "--ext",
        nargs="*",
        default=sorted(DEFAULT_INCLUDE_EXT),
        help="File extensions to include (e.g., .pdf .eml .txt)",
    )
    g.add_argument(
        "-I",
        "--include-glob",
        dest="include_globs",
        nargs="*",
        default=None,
        help="Only include files matching these glob patterns (relative paths)",
    )
    g.add_argument(
        "-X",
        "--exclude-glob",
        dest="exclude_globs",
        nargs="*",
        default=None,
        help="Exclude files matching these glob patterns (relative paths)",
    )

    c = sub.add_parser("check", help="Check a manifest against current files")
    c.add_argument("manifest", help="Path to manifest file")
    c.add_argument("--root", default=".", help="Project root (default: .)")

    return p.parse_args(argv)


def app_main(argv: List[str] | None = None) -> int:
    ns = _parse_args(argv)
    if ns.cmd == "generate":
        root = Path(ns.root)
        output = Path(ns.output)
        generate_manifest(
            root=root,
            output=output,
            include_ext=ns.ext,
            include_globs=ns.include_globs,
            exclude_globs=ns.exclude_globs,
        )
        print(f"Wrote manifest to {output}")
        return 0
    elif ns.cmd == "check":
        code, errors = check_manifest(Path(ns.manifest), Path(ns.root))
        if errors:
            for e in errors:
                print(e)
        if code == 0:
            print("Integrity OK: all files match manifest")
        return code
    else:
        raise SystemExit(2)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(app_main())
