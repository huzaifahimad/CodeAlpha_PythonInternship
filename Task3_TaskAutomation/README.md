# ⚙️ Task 3 — Task Automation with Python Scripts

> **CodeAlpha Python Internship | Task 3**

Three real-world automation scripts packaged as a single interactive suite. Each module solves a distinct repetitive task: organizing image files, extracting emails from text, and scraping webpage titles — all accessible via a clean menu-driven interface.

---

## 📋 Table of Contents

- [Modules](#-modules)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [How to Run](#-how-to-run)
- [Module Details](#-module-details)
- [Code Architecture](#-code-architecture)
- [Concepts Used](#-concepts-used)

---

## 🧩 Modules

| # | Module | What It Does |
|---|---|---|
| A | **File Organizer** | Moves all `.jpg` / `.jpeg` files from a source folder to a target folder |
| B | **Email Extractor** | Scans a `.txt` file and extracts all unique email addresses |
| C | **Web Scraper** | Fetches a webpage and extracts the `<title>` tag content |

---

## 📁 Project Structure

```
Task3_TaskAutomation/
│
├── automation.py          # All 3 modules + menu interface
├── README.md              # This file
└── output/                # Auto-created — holds all saved results
    ├── extracted_emails_YYYYMMDD_HHMMSS.txt
    └── scraped_title_YYYYMMDD_HHMMSS.txt
```

---

## ⚙️ Requirements

- Python **3.10+**
- `requests` — only required for **Module C** (Web Scraper)

```bash
pip install requests
```

Modules A and B use **standard library only** (`os`, `re`, `shutil`, `pathlib`).

---

## ▶️ How to Run

```bash
cd Task3_TaskAutomation
python automation.py
```

You will see the module selection menu:

```
  [1]  📁  File Organizer    — Move .jpg files to a folder
  [2]  📧  Email Extractor   — Extract emails from .txt
  [3]  🌐  Web Scraper       — Scrape a webpage title
  [4]  🚪  Exit
```

---

## 🔍 Module Details

### Module A — File Organizer

**Input:** Source directory path, target directory path  
**Behavior:**
- Scans source directory for `.jpg` / `.jpeg` files
- Creates the target directory if it doesn't exist
- Moves files without overwriting existing ones
- Reports moved / skipped / error counts

```
  Enter SOURCE directory path: /home/user/Downloads
  Enter TARGET directory path: /home/user/Images

  ✅  Moved: photo1.jpg  →  /home/user/Images
  ✅  Moved: photo2.jpeg →  /home/user/Images
  ⚠️  Skipped (already exists): photo3.jpg

  ─── Summary ───
  Moved   : 2
  Skipped : 1
  Errors  : 0
```

---

### Module B — Email Extractor

**Input:** Path to any `.txt` file  
**Behavior:**
- Reads the entire file
- Applies RFC-5321 regex to find all email patterns
- Deduplicates and sorts results
- Optionally saves to timestamped `.txt` output

```
  Enter path to .txt file: contacts.txt

  ✅  Found 4 unique email address(es):

      1. alice@example.com
      2. bob.smith@company.org
      3. info@codealpha.tech
      4. support@gmail.com
```

---

### Module C — Web Scraper

**Input:** URL (defaults to `https://www.python.org`)  
**Behavior:**
- Makes an HTTP GET request with a proper User-Agent header
- Extracts `<title>` tag using regex (no external HTML parser needed)
- Optionally saves the result to a timestamped `.txt` file

```
  Fetching: https://www.python.org ...

  ✅  Page Title Found:

      "Welcome to Python.org"
```

---

## 🏗️ Code Architecture

```
main()  ←  menu loop
 ├── run_file_organizer()
 │    ├── get_jpg_files()          → scans directory
 │    └── move_jpg_files()         → shutil.move with skip logic
 │
 ├── run_email_extractor()
 │    └── extract_emails_from_file() → regex + dedup + sort
 │
 └── run_web_scraper()
      └── scrape_page_title()      → requests.get + regex title

Shared Utilities
 ├── clear_screen()
 ├── print_banner()
 ├── log_success / log_warning / log_error / log_info
 └── save_results_to_txt()
```

---

## 🧠 Concepts Used

- `os` / `pathlib.Path` — directory traversal and path management
- `shutil.move()` — cross-platform file moving
- `re.compile()` / `re.search()` / `re.findall()` — regex for email and title extraction
- `requests` — HTTP GET with timeout and User-Agent header
- File handling — reading `.txt`, writing timestamped output files
- `sys.exit()` — clean program termination
- Type hints and docstrings — professional code documentation

---

*CodeAlpha Python Internship — Task 3*
