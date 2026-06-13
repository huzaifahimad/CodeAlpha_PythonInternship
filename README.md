# 🐍 CodeAlpha Python Internship — All Tasks

> **Intern:** Huzaifa Himad  
> **Student ID:** CA/DF1/101068  
> **Program:** CodeAlpha Python Programming Internship  
> **GitHub Repo:** `CodeAlpha_PythonInternship`

A complete collection of three Python internship projects, each built to a professional standard with clean architecture, full input validation, type hints, docstrings, and individual README documentation.

---

## 📁 Repository Structure

```
CodeAlpha_PythonInternship/
│
├── README.md                            ← You are here (master overview)
│
├── Task1_Hangman/
│   ├── hangman.py                       ← Hangman game
│   └── README.md
│
├── Task2_StockPortfolioTracker/
│   ├── stock_tracker.py                 ← Portfolio tracker
│   ├── README.md
│   └── output/                          ← Auto-created on export
│       ├── portfolio_report.csv
│       └── portfolio_report.txt
│
├── Task3_TaskAutomation/
│   ├── automation.py                    ← 3-module automation suite
│   ├── README.md
│   └── output/                          ← Auto-created on save
│       ├── extracted_emails_*.txt
│       └── scraped_title_*.txt

```

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/huzaifahimad/CodeAlpha_PythonInternship.git
cd CodeAlpha_PythonInternship

# Run any task directly
python Task1_Hangman/hangman.py
python Task2_StockPortfolioTracker/stock_tracker.py
python Task3_TaskAutomation/automation.py
```

---

## 📦 Dependencies

| Task | Dependencies |
|---|---|
| Task 1 — Hangman | Standard library only |
| Task 2 — Stock Tracker | Standard library only |
| Task 3 — Task Automation | `requests` (Module C only) |


Install the only external dependency:

```bash
pip install requests
```

> Python **3.10+** required for all tasks.

---

## 📋 Task Summaries

---

### 🎮 Task 1 — Hangman Game

**File:** `Task1_Hangman/hangman.py`

A complete terminal-based Hangman game with 7-stage ASCII art gallows, live word display, input validation, session scoring, and replay support.

**Highlights:**
- 7-stage ASCII hangman that builds in real-time
- Set-based O(1) lookup for guessed letters
- Win/loss score tracking across multiple rounds
- Cross-platform screen clearing

```bash
python Task1_Hangman/hangman.py
```

**Key Concepts:** `random`, `set`, `while` loop, `f-strings`, type hints, docstrings

---

### 📊 Task 2 — Stock Portfolio Tracker

**File:** `Task2_StockPortfolioTracker/stock_tracker.py`

A professional portfolio management tool tracking 10 real-world stocks. Users input tickers and quantities; the app calculates total value, portfolio weights, and exports to both CSV and TXT formats.

**Highlights:**
- 10 pre-loaded stocks (AAPL, TSLA, NVDA, MSFT, and more)
- `StockHolding` class with auto-computed position value
- Duplicate ticker prevention
- Timestamped CSV and TXT export with formatted tables

```bash
python Task2_StockPortfolioTracker/stock_tracker.py
```

**Key Concepts:** `dict`, `class`, `csv` module, file handling, `datetime`, type hints

---

### ⚙️ Task 3 — Task Automation Suite

**File:** `Task3_TaskAutomation/automation.py`

Three automation scripts in one interactive suite, selectable via a menu:

| Module | Function |
|---|---|
| A — File Organizer | Moves `.jpg` / `.jpeg` files from source to target folder |
| B — Email Extractor | Extracts unique emails from any `.txt` file via regex |
| C — Web Scraper | Fetches and saves the `<title>` tag from any webpage |

```bash
python Task3_TaskAutomation/automation.py
```

**Key Concepts:** `os`, `shutil`, `re`, `pathlib`, `requests`, file I/O, input validation

---



## 🏗️ Code Quality Standards

All tasks follow these professional standards:

| Standard | Implementation |
|---|---|
| Type Hints | All function signatures annotated |
| Docstrings | Every function/class documented |
| Constants | Uppercase module-level constants |
| Separation of Concerns | Logic, UI, and I/O in separate functions |
| Input Validation | All user inputs sanitized before use |
| Error Handling | `try/except` on all risky operations |
| Cross-Platform | Windows and Unix/Linux compatible |
| Clean Exit | Keyboard interrupt handled gracefully |

---

## 📬 Contact

- **GitHub:** [github.com/huzaifahimad](https://github.com/huzaifahimad)
- **LinkedIn:** [linkedin.com/in/huzaifa-himad-46bb75389](https://linkedin.com/in/huzaifa-himad-46bb75389)
- **Internship:** [codealpha.tech](https://www.codealpha.tech)

---

*CodeAlpha Python Internship — All 3 Tasks Complete*
