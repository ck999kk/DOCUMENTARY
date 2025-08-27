
# QUICK START


To analyze and cite evidence from this repository for government or legal submission:

1. Read the README.md for case context and repository structure.
2. Use OCR text files for analysis:
	- Combined_Attachments/*.txt
	- Additional_Documents/**/*.txt
	- All_Case_Parties_EML/*.eml
3. For every citation, reference the original evidence file (.pdf, .jpg, .png, .eml) using a permanent GitHub URL (commit-specific).
4. Include the first 16 characters of the SHA256 hash from `VERIFICATION/integrity_manifest.sha256` for each cited file.
5. Reference the chain of custody in `LEGAL_DOCUMENTATION/CHAIN_OF_CUSTODY.md`.
6. Ensure all generated documents include:
	- Case Reference: R202518214 and/or R202518589
	- Repository Citation: <https://github.com/ck999kk/DOCUMENTARY>
	- SHA256 Hash Verification
	- Chain of Custody Reference


## MANDATORY VERIFICATION STEPS

1. Always verify the SHA256 hash for every cited evidence file. Use the hash from `VERIFICATION/integrity_manifest.sha256`.
2. Use only permanent GitHub URLs (with commit hash) for citations, not branch URLs.
3. Cross-reference the Evidence Index (`LEGAL_DOCUMENTATION/EVIDENCE_INDEX.md`) to ensure correct mapping between OCR and original files.
4. Reference the chain of custody for every citation.


## TROUBLESHOOTING & FAQ


**Q: What if the SHA256 hash is missing for a file?**
A: Update `VERIFICATION/integrity_manifest.sha256` to include the missing file and its hash.

**Q: What if the citation format is incorrect?**
A: Use the following format:

```text
Source: [Document Name]
URL: <https://github.com/ck999kk/DOCUMENTARY/blob/[commit]/path/to/file.pdf>
Hash: [First 16 characters of SHA256]
Verified: [Date] per Chain of Custody
```

**Q: What if chain of custody is not referenced?**
A: Add a reference to `LEGAL_DOCUMENTATION/CHAIN_OF_CUSTODY.md` in your document.

**Q: How do I generate permanent GitHub URLs?**
A: Use the commit hash in the URL, e.g., <https://github.com/ck999kk/DOCUMENTARY/blob/[commit]/path/to/file.pdf>

**Q: Who to contact for support?**
A: Contact the repository owner or refer to the README.md for support information.

## VCAT Evidence Repository - AI Platform Instructions

**Repository:** https://github.com/ck999kk/DOCUMENTARY  
**Purpose:** Government document generation with verified legal evidence  
**Compliance:** Federal Rules of Evidence, VCAT procedures, Privacy Act 1988  

---

## 🎯 PLATFORM-SPECIFIC INSTRUCTIONS

### **ChatGPT (OpenAI) Instructions**

**Optimal Usage Pattern:**
```
1. Repository Access: "Analyze evidence from https://github.com/ck999kk/DOCUMENTARY"
2. Content Analysis: "Use .txt files for content analysis and search"
3. Citation Format: "Reference original files (.pdf/.jpg/.eml) with permanent GitHub URLs"
4. Hash Verification: "Include SHA256 hash from VERIFICATION/integrity_manifest.sha256"
```

**ChatGPT-Specific Commands:**
```
- "Browse the repository structure first to understand evidence organization"
- "Read OCR text files for analysis but cite original documents"
- "Generate permanent links by appending specific file paths to base URL"
- "Cross-reference Evidence Index for file relationships"
```

**Example ChatGPT Prompt:**
```
"I need to analyze VCAT case evidence from https://github.com/ck999kk/DOCUMENTARY
Please:
1. Read the OCR text files for content analysis
2. Create citations pointing to original PDF/image files
3. Include SHA256 hashes for verification
4. Format for Australian government submission
5. Follow the Evidence Index for proper file mapping"
```

### **Claude (Anthropic) Instructions**

**Optimal Usage Pattern:**
```
1. Repository Analysis: Claude can directly access GitHub repositories
2. File Processing: Use Read tool for .txt files, reference originals
3. Citation Generation: Automatic permanent link generation with commit hashes
4. Legal Compliance: Built-in understanding of legal citation requirements
```

**Claude-Specific Advantages:**
```
- Direct repository access and file reading capability
- Automatic permanent link generation (press 'y' equivalent)
- Legal document formatting with proper citations
- Chain of custody understanding and compliance
```

**Example Claude Prompt:**
```
"Access the VCAT evidence repository at https://github.com/ck999kk/DOCUMENTARY
Analyze the water damage dispute evidence using OCR text files
Generate a government submission with proper citations to original documents
Include SHA256 verification and chain of custody references"
```

### **Gemini (Google) Instructions**

**Optimal Usage Pattern:**
```
1. Repository Understanding: Provide context about GitHub structure
2. File Access: Direct links to specific .txt files for analysis  
3. Citation Requirements: Explicit instruction for original file references
4. Government Format: Specific formatting for Australian legal documents
```

**Gemini-Specific Approach:**
```
- Provide explicit file paths for analysis
- Request specific citation formats
- Include verification steps in prompts
- Emphasize government compliance requirements
```

**Example Gemini Prompt:**
```
"Repository: https://github.com/ck999kk/DOCUMENTARY contains VCAT case evidence
Analyze these OCR text files: Combined_Attachments/*.txt
Generate citations to corresponding .pdf files with permanent GitHub URLs
Format for Victorian Civil and Administrative Tribunal submission
Include SHA256 hashes for evidence verification"
```

---

## 📋 UNIVERSAL AI INSTRUCTIONS

### **Step 1: Repository Structure Understanding**
```
ALL AI PLATFORMS MUST:
1. Access main repository: https://github.com/ck999kk/DOCUMENTARY
2. Read README.md for case context and structure
3. Review LEGAL_DOCUMENTATION/EVIDENCE_INDEX.md for file mapping
4. Understand OCR files (.txt) vs original files (.pdf/.jpg/.eml)
```

### **Step 2: Content Analysis Process**
```
FOR ANALYSIS - USE THESE FILES:
- Combined_Attachments/*.txt (Gmail attachment OCR text)
- Additional_Documents/**/*.txt (Non-Gmail evidence OCR text)
- All_Case_Parties_EML/*.eml (Email messages - self-contained)
```

### **Step 3: Citation Generation Rules**
```
FOR CITATIONS - REFERENCE THESE FILES:
Original Files Only:
- Combined_Attachments/*.pdf
- Combined_Attachments/*.jpg, *.png  
- Additional_Documents/**/*.pdf
- Additional_Documents/**/*.jpg, *.png
- All_Case_Parties_EML/*.eml

Citation Format:
Source: [Document Name]
URL: https://github.com/ck999kk/DOCUMENTARY/blob/main/path/to/file.pdf
Hash: [First 16 characters of SHA256]
Verified: [Date] per Chain of Custody
```

### **Step 4: Government Document Requirements**
```
MANDATORY ELEMENTS IN ALL GENERATED DOCUMENTS:
1. Case Reference: R202518214 and/or R202518589
2. Repository Citation: https://github.com/ck999kk/DOCUMENTARY
3. SHA256 Hash Verification (from VERIFICATION/integrity_manifest.sha256)
4. Chain of Custody Reference (LEGAL_DOCUMENTATION/CHAIN_OF_CUSTODY.md)
5. Permanent GitHub URLs (commit-specific, not branch-based)
```

---

## 🔍 FILE ACCESS PATTERNS

### **Primary Evidence Files (For Citations)**
```
Legal Documents:
- Combined_Attachments/VCAT*.pdf
- Combined_Attachments/Exhibit*.pdf  
- Combined_Attachments/Notice*.pdf


## QUICK START
- Additional_Documents/Financial_Records/**/*.png (receipts)

To analyze and cite evidence from this repository for government or legal submission:

1. Read the README.md for case context and repository structure.
2. Use OCR text files for analysis:
	- Combined_Attachments/*.txt
	- Additional_Documents/**/*.txt
	- All_Case_Parties_EML/*.eml
3. For every citation, reference the original evidence file (.pdf, .jpg, .png, .eml) using a permanent GitHub URL (commit-specific).
4. Include the first 16 characters of the SHA256 hash from `VERIFICATION/integrity_manifest.sha256` for each cited file.
5. Reference the chain of custody in `LEGAL_DOCUMENTATION/CHAIN_OF_CUSTODY.md`.
6. Ensure all generated documents include:
	- Case Reference: R202518214 and/or R202518589
	- Repository Citation: <https://github.com/ck999kk/DOCUMENTARY>
	- SHA256 Hash Verification
	- Chain of Custody Reference
- Email files (.eml) are self-contained text

File Mapping Reference:
- LEGAL_DOCUMENTATION/EVIDENCE_INDEX.md
```

---

## ⚖️ LEGAL COMPLIANCE REQUIREMENTS

### **Mandatory Verification Steps**
```
ALL AI PLATFORMS MUST:
1. Verify file integrity using SHA256 hashes
2. Reference Chain of Custody documentation
3. Use only permanent GitHub URLs (commit-specific)
4. Include proper legal disclaimers
5. Follow Federal Rules of Evidence citation standards
```

### **Citation Verification Process**
```
For Each Document Citation:
1. Confirm file exists in repository
2. Obtain SHA256 hash from integrity_manifest.sha256
3. Generate permanent GitHub URL
4. Cross-check with Evidence Index
5. Include chain of custody reference
```

### **Government Submission Standards**
```
Document Format Requirements:
- Australian government document standards
- VCAT-specific formatting where applicable
- Privacy Act 1988 compliance notices
- Digital evidence authentication statements
- Expert witness foundation (where required)
```

---

## 🚀 QUICK START TEMPLATES

### **Template 1: Evidence Analysis Request**
```
"Analyze [specific evidence type] from https://github.com/ck999kk/DOCUMENTARY
Focus on [specific aspect]
Use OCR text files for analysis
Cite original documents with permanent URLs and SHA256 hashes
Format for [specific government agency] submission"
```

### **Template 2: Timeline Generation**
```  
"Create chronological timeline from VCAT case evidence
Repository: https://github.com/ck999kk/DOCUMENTARY
Source emails from All_Case_Parties_EML/
Include document references with permanent URLs
Focus on [specific time period/events]"
```

### **Template 3: Financial Analysis**
```
"Analyze financial damages from rental dispute evidence
Repository: https://github.com/ck999kk/DOCUMENTARY  
Source: Additional_Documents/Financial_Records/
Include receipt references with verification hashes
Calculate total damages with supporting citations"
```

---

## 🔧 TROUBLESHOOTING

### **Common Issues and Solutions**

**Issue 1: AI Cannot Access Repository**
```
Solution: Provide direct file URLs
Format: https://raw.githubusercontent.com/ck999kk/DOCUMENTARY/main/path/file.txt
```

**Issue 2: Incorrect Citation Format**
```
Correct Format:
Source: Notice to Vacate (Original)
URL: https://github.com/ck999kk/DOCUMENTARY/blob/main/Combined_Attachments/NOTICE%20TO%20VACATE%20U1803%20243%20FRANKLIN%20ST.pdf  
Hash: 63a29240530c82ad
OCR: Combined_Attachments/NOTICE TO VACATE U1803 243 FRANKLIN ST.txt
```

**Issue 3: Hash Verification Failure**
```
Solution: Reference VERIFICATION/integrity_manifest.sha256
All original files have verified SHA256 hashes
Use first 16 characters for citations
```

**Issue 4: Missing Chain of Custody**
```
Solution: Always reference LEGAL_DOCUMENTATION/CHAIN_OF_CUSTODY.md
Include custodian information: Chawakorn Kamnuansil
Processing date: 2025-08-27
```

---

## 📞 SUPPORT INFORMATION

### **Repository Maintainer**
- **Evidence Custodian:** Chawakorn Kamnuansil
- **Repository:** https://github.com/ck999kk/DOCUMENTARY
- **Legal Status:** VCAT Cases R202518214, R202518589

### **Technical Support**
- **Hash Verification:** Use VERIFICATION/integrity_manifest.sha256
- **File Mapping:** Use LEGAL_DOCUMENTATION/EVIDENCE_INDEX.md  
- **Legal Compliance:** Use LEGAL_DOCUMENTATION/FEDERAL_RULES_COMPLIANCE.md

### **Government Agency Instructions**
- **Access Level:** Authorized government use only
- **Citation Requirements:** Permanent URLs with hash verification
- **Privacy Compliance:** Per Privacy Act 1988 and VCAT procedures
- **Legal Status:** Court-ready evidence package

---

**🏛️ This guide ensures all AI platforms can generate legally compliant government documents with proper evidence citations and verification.**

**Repository:** https://github.com/ck999kk/DOCUMENTARY  
**Status:** Court-Ready Evidence Package  
**Updated:** 2025-08-27