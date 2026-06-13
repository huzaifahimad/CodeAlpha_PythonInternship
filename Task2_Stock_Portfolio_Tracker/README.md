# 📊 Task 2 — Stock Portfolio Tracker

> **CodeAlpha Python Internship | Task 2**

A professional terminal-based stock portfolio tracker. Users input stock tickers and share quantities; the program calculates total investment value, displays a weighted portfolio table, and optionally exports the report to both `.csv` and `.txt` formats.

---

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [How to Run](#-how-to-run)
- [Usage Demo](#-usage-demo)
- [Output Files](#-output-files)
- [Code Architecture](#-code-architecture)
- [Concepts Used](#-concepts-used)

---

## ✨ Features

| Feature | Description |
|---|---|
| 10 Real Stocks | AAPL, TSLA, GOOGL, MSFT, AMZN, NVDA, META, NFLX, AMD, INTC |
| Portfolio Table | Shows ticker, quantity, price, value, and portfolio weight |
| Duplicate Guard | Prevents adding the same stock twice |
| CSV Export | Saves structured report with headers and timestamps |
| TXT Export | Saves a human-readable plain-text report |
| Input Validation | Rejects invalid tickers, non-numeric and zero quantities |
| OOP Design | `StockHolding` dataclass for clean data encapsulation |

---

## 📁 Project Structure

```
Task2_StockPortfolioTracker/
│
├── stock_tracker.py         # Main application
├── README.md                # This file
└── output/                  # Auto-created on first export
    ├── portfolio_report.csv
    └── portfolio_report.txt
```

---

## ⚙️ Requirements

- Python **3.10+**
- No third-party libraries — **standard library only** (`csv`, `os`, `datetime`)

---

## ▶️ How to Run

```bash
cd Task2_StockPortfolioTracker
python stock_tracker.py
```

---

## 🖥️ Usage Demo

```
  Available Stocks

  Ticker   Company / Description          Price (USD)
  ────────────────────────────────────────────────────
  AAPL     Apple Inc.                      $189.30
  TSLA     Tesla Inc.                      $248.50
  NVDA     NVIDIA Corporation              $875.40
  ...

  Ticker symbol (or DONE to finish): AAPL
  Quantity of AAPL shares: 10
  ✅  Added: 10 × AAPL @ $189.30 = $1,893.00

  Ticker symbol (or DONE to finish): NVDA
  Quantity of NVDA shares: 5
  ✅  Added: 5 × NVDA @ $875.40 = $4,377.00

  Ticker symbol (or DONE to finish): DONE

  ──────────────────────────────────────────────────────
  #    Ticker      Qty    Price (USD)    Value (USD)  Weight
  ─────────────────────────────────────────────────────────
  1    AAPL         10      $189.30       $1,893.00   30.2%
  2    NVDA          5      $875.40       $4,377.00   69.8%
  ─────────────────────────────────────────────────────────
  TOTAL                                  $6,270.00  100.0%

  💰  Total Portfolio Value: $6,270.00
```

---

## 📄 Output Files

### CSV (`output/portfolio_report.csv`)
```csv
Generated,2024-01-15 14:30:22

Ticker,Quantity,Price (USD),Value (USD),Weight (%)
AAPL,10,189.30,1893.00,30.20
NVDA,5,875.40,4377.00,69.80

TOTAL,,,6270.00,100.00
```

### TXT (`output/portfolio_report.txt`)
A formatted, human-readable version of the same data.

---

## 🏗️ Code Architecture

```
main()
 ├── print_available_stocks()    → lists all 10 stocks
 ├── build_portfolio()
 │    ├── get_ticker()           → validated ticker input
 │    └── get_quantity()         → validated share count
 ├── print_portfolio_table()     → renders formatted table
 ├── export_to_csv()             → CSV file output
 └── export_to_txt()             → TXT file output

StockHolding (class)
 └── ticker, quantity, price, value
```

---

## 🧠 Concepts Used

- `dict` — hardcoded stock price lookup table
- `class` — `StockHolding` data model with auto-computed `value`
- `csv` module — structured CSV file export
- File handling (`open`, `write`) — plain-text report export
- `os.makedirs()` — output directory management
- `datetime` — timestamping reports
- Input validation — ticker checking, integer parsing
- Type hints — full annotation throughout

---

*CodeAlpha Python Internship — Task 2*
