# DOCUMENTARY: Evidence & Legal Documentation Toolkit

Evidence management for legal and AI workflows.
- Automates SHA256 verification
- Creates permanent commit-pinned URLs for citations
- Provides templates and scripts for document generation

[![Legal Grade](https://img.shields.io/badge/Legal-Grade-red)](https://github.com/ck999kk/DOCUMENTARY)
[![Evidence Integrity](https://img.shields.io/badge/Evidence-Verified-green)](./VERIFICATION/)
[![Chain of Custody](https://img.shields.io/badge/Chain%20of%20Custody-Complete-blue)](./LEGAL_DOCUMENTATION/)

---

## 🤝 Contributing

See `AGENTS.md` for contributor guidelines, coding style, and CI gates.

---

## 📦 Quick Start

- **For AI:** Use `.txt` OCR files for analysis.
- **For Legal:** Cite original files with commit-pinned GitHub URLs and SHA256 hashes.
- **For Everyone:** See `LEGAL_DOCUMENTATION/EVIDENCE_INDEX.md` for file relationships.

---

## 📂 Repository Structure

- `LEGAL_DOCUMENTATION/` – Chain of custody, evidence index, exhibits
- `VERIFICATION/` – SHA256 manifest for integrity checks
- `All_Case_Parties_EML/` – Email evidence
- `Combined_Attachments/` – Attachments + OCR text
- `Additional_Documents/` – Extra evidence, financial, supporting docs
- `tools/` – Scripts for citation and table generation

---

## 🔒 Integrity Check

Run from the repository root to verify against the manifest:

```bash
# macOS/Linux
shasum -a 256 -c VERIFICATION/integrity_manifest.sha256
```

Notes:
- The manifest intentionally excludes itself and volatile files (e.g., `.DS_Store`).
- If files change, regenerate the manifest from repo root:
  `find . -type f -not -name '.DS_Store' -not -path './.git/*' -not -path './.venv/*' -not -path './VERIFICATION/integrity_manifest.sha256' -print0 | xargs -0 shasum -a 256 > VERIFICATION/integrity_manifest.sha256`

---

## 📝 Citation Example

```
Source: [Document Name]
URL: https://github.com/ck999kk/DOCUMENTARY/blob/[commit]/path/to/file.pdf
Hash: [First 16 characters of SHA256]
Verified: [Date] per Chain of Custody
```

---

## 🤖 AI Usage

- Use OCR `.txt` files for analysis/search
- Reference original files for citations
- Always include SHA256 hash and chain of custody

---

## 🤖 For AI Agents

- Start here: `LEGAL_DOCUMENTATION/EVIDENCE_INDEX.md` (maps originals ↔ OCR text with SHA256).
- Exhibits: `LEGAL_DOCUMENTATION/EXHIBITS_commit_pinned.md` and `.csv` (commit‑pinned URLs + hashes).
- Chain of Custody: `LEGAL_DOCUMENTATION/CHAIN_OF_CUSTODY.md` (handling timeline and verification notes).
- Integrity: `VERIFICATION/integrity_manifest.sha256` and quick check via `tools/verify.sh check`.
- Citations: `LEGAL_DOCUMENTATION/CITATIONS.md` (ready‑to‑copy citation blocks).

Notes for agents:
- Do not alter originals; derivatives live alongside and are referenced in legal docs.
- When new evidence is added, regenerate manifest with `tools/verify.sh update` and update Exhibits.

## 📋 Evidence Types

- Property, financial, communication, legal documents

---

## 📞 Contact

Evidence Custodian: Chawakorn Kamnuansil  
Access: By legal request only

---

## ⚠️ DISCLAIMER

This repository is provided for legal, government, and AI-assisted evidence management purposes only. Unauthorized access, use, or distribution is strictly prohibited. All information is provided as-is, without warranty of any kind. Users are responsible for compliance with all applicable laws and regulations.

---

*Prepared in accordance with VCAT Evidence and Procedure Rules*
