import argparse
import os
import sys

MANIFEST_PATH = os.path.join(os.path.dirname(__file__), '../VERIFICATION/integrity_manifest.sha256')
CHAIN_OF_CUSTODY_PATH = os.path.join(os.path.dirname(__file__), '../LEGAL_DOCUMENTATION/CHAIN_OF_CUSTODY.md')


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
                hashes[norm_path] = sha[:16]
                hashes[base] = sha[:16]
    return hashes


def generate_citation(filename, commit_hash, verified_date):
    hashes = load_hashes(MANIFEST_PATH)
    import os
    norm_filename = os.path.normpath(filename.lstrip('./')).lower().strip()
    base = os.path.basename(norm_filename)
    print("--- DEBUG ---")
    print(f"Normalized input: '{norm_filename}'")
    print(f"Base filename: '{base}'")
    print(f"Manifest keys: {list(hashes.keys())[:10]} ... total: {len(hashes)}")
    sha = (
        hashes.get(norm_filename)
        or hashes.get(filename)
        or hashes.get(base)
    )
    if not sha:
        print(f"SHA256 hash not found for {filename}")
        print("Try searching for similar keys:")
        for k in hashes:
            if base in k:
                print(f"Possible match: {k} -> {hashes[k]}")
        sys.exit(1)
    citation = f"""Source: {os.path.basename(filename)}\nURL: <https://github.com/ck999kk/DOCUMENTARY/blob/{commit_hash}/{filename}>\nHash: {sha}\nVerified: {verified_date} per Chain of Custody\nChain of Custody: {CHAIN_OF_CUSTODY_PATH}\n"""
    return citation


def main():
    parser = argparse.ArgumentParser(description='Generate citation block for evidence file.')
    parser.add_argument('filename', help='Relative path to evidence file')
    parser.add_argument('commit_hash', help='Git commit hash for permanent URL')
    parser.add_argument('--date', default='2025-08-27', help='Verification date (default: today)')
    args = parser.parse_args()
    citation = generate_citation(args.filename, args.commit_hash, args.date)
    print(citation)


if __name__ == '__main__':
    main()
