from pathlib import Path

from verify.cli import (
    check_manifest,
    generate_manifest,
    load_manifest,
    sha256_file,
)


def write(p: Path, data: bytes) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)


def test_generate_and_check(tmp_path: Path) -> None:
    root = tmp_path
    a = root / "docs" / "a.txt"
    b = root / "docs" / "b.pdf"
    write(a, b"hello")
    write(b, b"%PDF-1.4\n")

    manifest = root / "VERIFICATION" / "integrity_manifest.sha256"
    entries = generate_manifest(root, manifest, include_ext=[".txt", ".pdf"])
    assert (manifest).exists()
    assert len(entries) == 2

    code, errors = check_manifest(manifest, root)
    assert code == 0
    assert errors == []

    # mutate one file -> should detect mismatch
    write(a, b"HELLO")
    code2, errors2 = check_manifest(manifest, root)
    assert code2 == 1
    assert any("MISMATCH" in e for e in errors2)


def test_include_exclude_globs(tmp_path: Path) -> None:
    root = tmp_path
    keep = root / "Combined_Attachments" / "good.txt"
    drop_tmp = root / "Combined_Attachments" / "ignore.tmp.txt"
    drop_dir = root / "drafts" / "note.txt"

    write(keep, b"ok")
    write(drop_tmp, b"ignore")
    write(drop_dir, b"ignore")

    manifest = root / "VERIFICATION" / "integrity_manifest.sha256"
    entries = generate_manifest(
        root,
        manifest,
        include_ext=[".txt"],
        include_globs=["Combined_Attachments/**"],
        exclude_globs=["**/*.tmp.txt", "**/drafts/**"],
    )
    # only the 'keep' file should be present
    assert [rel for (_, rel) in entries] == ["Combined_Attachments/good.txt"]
