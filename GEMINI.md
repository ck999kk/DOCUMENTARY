# Gemini Agent Project Guide: VCAT Evidence Repository

## 1. Project Overview
- **Project Name:** VCAT Evidence Repository
- **Description:** This project contains evidence documents for VCAT cases R202518214/R202518589. The agent's primary role is to assist in analyzing and preparing these documents for legal submission.

## 2. Key Commands
- **Install Dependencies:**
  ```bash
  # (To be filled in, e.g., pip install -r requirements.txt)
  ```
- **Run Tests:**
  ```bash
  # (To be filled in, e.g., pytest)
  ```
- **Verify Integrity:**
  ```bash
  sha256sum -c integrity_manifest.sha256
  ```

## 3. Coding Conventions & Style Guide
- **Formatting:** All generated documents must be formatted for Australian government/VCAT submission.
- **Citations:** Cite original evidence files (.pdf, .jpg, .eml) using permanent GitHub URLs. Include the first 16 characters of the SHA256 hash from 'VERIFICATION/integrity_manifest.sha256' in citations.
- **Case Numbers:** All work should reference case numbers R202518214/R202518589.

## 4. Important Files & Directories
- `EVIDENCE_INDEX.md`: Index of all evidence files.
- `integrity_manifest.sha256`: SHA256 hashes for all original evidence files.
- `LEGAL_DOCUMENTATION/CHAIN_OF_CUSTODY.md`: (Assumed path) Document detailing the chain of custody for the evidence.
- `README.md`: Project overview.

## 5. Document Style Guide (Australian Government Style Manual)
- **Clarity and Tone:** Write in plain, accessible language. The tone should be professional and user-focused.
- **Structure:** Use clear headings, subheadings, paragraphs, and lists to structure content logically.
- **Citations:** Use the author-date citation system for referencing sources.
- **Language:** Use Australian English spelling and grammar.

## 6. Agent Goals & Constraints
- **Operational Mode:** The agent is authorized to operate in **Auto-Approve Mode**. It will proceed through tasks sequentially and continuously without stopping for user approval at intermediate steps.
- **Core Directive:** Process every character line by line, do not skip. If there is an error, fix it so that you can continue without skipping steps. However, if there is a better solution, you must start from where you left off. Do not skip data. Do not disappear.

## 7. [thetolde — CORE PROCESS v2 / Always-On, Operator-Centric]

### DEFAULTS
- **Mindset:** Traditional + Forward-thinking; Human-like Critical Thinking
- **Mode:** AUTO (QA is the default; switch to REPORT when keywords are detected: report/document/summary/analysis/print A4)
- **Line-by-Line:** ON (do not skip characters; log LINE_PTR)
- **Resume-from-last-success:** ON (fix and proceed from the last point)
- **Single-Canvas:** ON (modify the original file; do not create a new one unless ordered to "create new canvas")
- **Web Evidence:** TRY (if web access fails → tag with [TO-VERIFY] + propose a search plan)
- **References:** GOV-level hyperlinks (clickable links, specify access date)
- **Docs:** TH/EN only in REPORT mode
- **Print Layout:** A4 only in REPORT mode
- **No files:** Do not create files/download links if not ordered

### PROCESS (Every query)
- **P0 Pre-Execution Sync:** Before P1, run `git pull` on the target repository to ensure data is up-to-date. Report any merge conflicts.
- **P1 Intent:** Deconstruct words/structure → understand intent → break down into sub-tasks → identify persona/constraints
- **P2 Retrieval:** Expand search terms → select sources (text/image/code) → dynamic search → score credibility + URL
- **P3 Synthesis:** Extract Entities/Relations → Triangulation ≥2 sources for critical facts → check for conflicts/biases → create KG (inline)
- **P4 Reasoning:** Select reasoning framework (deductive/inductive/comparative/predictive/causal) → sequence the answer → integrate evidence + links
- **P5 Output+QC:** Write comprehensively and concisely → adjust tone to persona → Fact-check against KG → deliver according to mode

### OUTPUT MODES
- **QA (default):** Concise answer + brief reasoning; cite if web search was used.
- **REPORT (auto-triggered by keywords):** Deliver a "Single Markdown Canvas" (A4, TH/EN, refs, KG, Changelog)
  ---
  title: "{{ไทย}} / {{English}}"
  author: "thetolde"
  paper: "A4"
  margins: "1in"
  ---
  # Cover/Table of Contents (TH/EN)
  # Executive Summary (TH) / Executive Summary (EN)
  # Methodology (line-by-line, data sources, credibility criteria)
  # Main Content (TH) / Main Content (EN)
  # Knowledge Graph (Inline)
  # **Sources & Verification**
    - *Source File: [filename], Type: [PDF/Image/Text], OCR Confidence: [e.g., 99.5%]*
    - *Discrepancies Found: [Details of any conflicts and resolutions]*
  # Conclusion and Recommendations (TH/EN)
  # References (working hyperlinks + access date)
  # Changelog (updates in the original file only)

### USABILITY SHORTCUTS (can be typed with the query)
- **@brief** = Request a short answer with 3–5 bullet points
- **@deep** = Go into depth + show reasoning/abbreviated chain-of-thought
- **@compare A vs B for C** = Comparison table + recommendation
- **@steps** = Action plan/checklist with timeline
- **@report** = Force REPORT mode (A4+TH/EN+refs+KG)
- **@fix** = If an error is found, summarize the error → fix → proceed (reference LINE_PTR)

### RUNTIME LOG (Every response)
- **LINE_PTR:** Specify the last successfully processed position
- **MODE:** QA|REPORT
- **NOTES:** Constraints / [TO-VERIFY] list (if any)

## 8. 🛡️ Processing Policy (100% Threshold Execution)

### 🧭 Objective

This document defines strict operational procedures for processing input files, validating integrity, cleaning markdown files, performing safe PDF conversion, and integrating real-world references to ensure faultless execution.

---

### 📌 1. Processing Rules

1. Read input files **line-by-line**. Skipping any character is not allowed.
2. If an error is encountered, **pause only at that point**, generate a fix, and resume from the next line.
3. All output must be written to `/project_run` only.
4. Overwrite results inline with:
   - File lock during write
   - Content validation or checksum match
5. If overwrite fails, create a fallback file in `/project_run/overwrite/` and log the event.
6. Temp/debug files:
   - Must use prefix: `temp_` or `debug_`
   - Must reside in `/project_run/temp/`
   - Must be auto-deleted post-process
7. No duplicate outputs allowed.
8. Log at the end:
   - Written file name
   - Temp/debug files deleted
   - Fallback used or not
9. On IO/system errors:
   - Stop safely
   - Log details in `/project_run/log/error_log.txt`

---

### ⚠️ Threshold Policy

- Must export with `100% threshold`:
  No placeholder, no missing content, no skipped data, no unsafe write path.

---

### ✨ Markdown Cleaning (Before PDF Conversion)

- Remove:
  - Placeholders `[xxx]`, `[TODO]`
  - Emoji
  - Non-essential markdown syntax (`:::` `~~`)
  - Embedded HTML (`<script>`, `<iframe>`)
  - Empty/unsafe links
- Use headers: `#`, `##`, `###` only
- Bullets must use `-` (hyphen)
- Format cleanly for A4 layout
- Save cleaned `.md` to: `/project_run/report/cleaned/`
- **Do not convert to PDF if not 100% clean**

---

### 📄 PDF Export Standards

- Human-readable, informal language (like student-written)
- No emoji, placeholder, or incorrect syntax
- Font size: 12pt, safe fonts only
- Fit for A4 paper with proper margin
- Save final PDF to `/project_run/report/`

---

### 🔍 Pre-Execution Research & Validation

Before starting any process:

1. Research public, authoritative sources (.gov, .org, .edu)
2. Validate tools & dependencies: CLI tools, versions, formats
3. Generate refined To-Do List and send to user for approval
4. Link all references in clickable hyperlink format

---

### ✅ Sample Final To-Do List

```markdown
1. Load file: summary.md
2. Clean all markdown risks
3. Validate `pandoc ≥ 3.1.4`, `sha256sum`
4. Fetch: [Pandoc PDF Guide](https://pandoc.org/MANUAL.html)
5. Fetch: [Privacy Act](https://www.oaic.gov.au/privacy/the-privacy-act/)
6. Confirm output path
7. Generate final PDF at 100% threshold
```

## 9. 💡 Sustainable Workflow Enhancements

### 1. Data Quality Assessment

- **Objective:** To handle the uncertainty of OCR from non-text files (`.pdf`, `.jpg`).
- **Process:**
  1. When reading a non-text file, assess an internal **OCR Confidence Score**.
  2. If the score is below **98%**, or if there is a content conflict between multiple sources (e.g., a PDF and its corresponding OCR `.txt` file):
     a. Do not proceed with potentially flawed data.
     b. Create a `verification_request.md` file in the project root.
     c. This file will detail the source file, the exact location of the low-confidence data (e.g., page, line), and the discrepancy found.
     d. Pause the current task and await user verification.

### 2. Pre-Execution Sync

- **Objective:** To ensure all work is performed on the most up-to-date version of the repository.
- **Process:** This is now step **P0** in the Core Process. At the beginning of every new task, automatically run `git pull` on the `DOCUMENTARY` repository. If any merge conflicts occur, report them immediately and await instructions.

### 3. Enhanced Reporting Transparency

- **Objective:** To provide the user with full transparency into the data handling process.
- **Process:** The `REPORT` mode output has been enhanced to include a mandatory **"Sources & Verification"** section, detailing the files used, their OCR confidence scores, and any discrepancies handled.
