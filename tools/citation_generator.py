import argparse
import csv
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = str(REPO_ROOT / 'VERIFICATION' / 'integrity_manifest.sha256')
CHAIN_OF_CUSTODY_PATH = str(REPO_ROOT / 'LEGAL_DOCUMENTATION' / 'CHAIN_OF_CUSTODY.md')


def load_hashes(manifest_path):
    import os
    hashes = {}
    with open(manifest_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                sha, path = parts
                # Normalize: remove leading './', convert to absolute, lower-case
                norm_path = os.path.normpath(path.lstrip('./')).lower()
                base = os.path.basename(norm_path)
                hashes[norm_path] = sha[:64]
                hashes[base] = sha[:64]
    return hashes


def generate_citation(filename, commit_hash, verified_date):
    hashes = load_hashes(MANIFEST_PATH)
    import os
    norm_filename = os.path.normpath(filename.lstrip('./')).lower().strip()
    base = os.path.basename(norm_filename)
    # Debug prints removed for clean CLI usage
    sha = (
        hashes.get(norm_filename)
        or hashes.get(filename)
        or hashes.get(base)
    )
    if not sha:
        print(f"Error: SHA256 hash not found for {filename}", file=sys.stderr)
        # Suggest similar keys (best-effort)
        suggestions = [k for k in hashes if base in k]
        if suggestions:
            print("Suggestions:", *suggestions[:10], sep="\n- ", file=sys.stderr)
        sys.exit(1)
    citation = (
        f"Source: {os.path.basename(filename)}\n"
        f"URL: https://github.com/ck999kk/DOCUMENTARY/blob/{commit_hash}/{filename}\n"
        f"Hash: {sha}\n"
        f"Verified: {verified_date} per Chain of Custody\n"
    )
    return citation


def generate_citations_from_exhibits_csv(csv_path: str, commit_hash: str, verified_date: str) -> str:
    hashes = load_hashes(MANIFEST_PATH)
    rows = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # Expected headers: No.,Title,Type,CommitPinnedURL,SHA256,RelativePath,Notes
        for r in reader:
            rel = (r.get('RelativePath') or '').strip()
            title = (r.get('Title') or os.path.basename(rel)).strip()
            if not rel:
                continue
            norm = os.path.normpath(rel.lstrip('./')).lower()
            base = os.path.basename(norm)
            sha = hashes.get(norm) or hashes.get(base)
            if not sha:
                continue
            url = f"https://github.com/ck999kk/DOCUMENTARY/blob/{commit_hash}/{rel}"
            rows.append((title, url, sha))
    out_lines = [
        "# Citations (commit-pinned)",
        f"Verified: {verified_date}",
        "",
    ]
    for idx, (title, url, sha) in enumerate(rows, 1):
        out_lines += [
            f"{idx}) {title}",
            "", 
            "```", 
            f"Source: {title}",
            f"URL: {url}",
            f"Hash: {sha}",
            f"Verified: {verified_date} per Chain of Custody",
            "```",
            "",
        ]
    return "\n".join(out_lines)


def main():
    parser = argparse.ArgumentParser(description='Generate citation(s) for evidence files.')
    sub = parser.add_subparsers(dest='cmd')

    p_one = sub.add_parser('one', help='Generate a single citation block')
    p_one.add_argument('filename', help='Relative path to evidence file')
    p_one.add_argument('commit_hash', help='Git commit hash for permanent URL')
    p_one.add_argument('--date', required=True, help='Verification date (e.g., 2025-08-28)')

    p_batch = sub.add_parser('batch', help='Generate citations from exhibits CSV')
    p_batch.add_argument('--from-exhibits', required=True, help='Path to EXHIBITS_commit_pinned.csv')
    p_batch.add_argument('--commit', required=True, help='Git commit hash for URLs')
    p_batch.add_argument('--output', required=True, help='Output Markdown path (e.g., LEGAL_DOCUMENTATION/CITATIONS.md)')
    p_batch.add_argument('--date', required=True, help='Verification date (e.g., 2025-08-28)')

    args = parser.parse_args()
    if args.cmd == 'one':
        print(generate_citation(args.filename, args.commit_hash, args.date))
    elif args.cmd == 'batch':
        text = generate_citations_from_exhibits_csv(args.from_exhibits, args.commit, args.date)
        out = Path(args.output)
        out.write_text(text, encoding='utf-8')
        print(f"Wrote citations to {out}")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
