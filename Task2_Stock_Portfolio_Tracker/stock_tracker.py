"""
Task 2 — Stock Portfolio Tracker
CodeAlpha Python Programming Internship

A terminal-based stock portfolio tracker with formatted tables,
portfolio weight calculation, and CSV/TXT export.
"""

import csv
import os
from datetime import datetime

# ── Hardcoded stock prices (USD) ───────────────
STOCK_PRICES: dict[str, float] = {
    "AAPL":  189.30,
    "TSLA":  248.50,
    "GOOGL": 175.20,
    "MSFT":  415.60,
    "AMZN":  185.90,
    "NVDA":  875.40,
    "META":  490.10,
    "NFLX":  605.70,
    "AMD":   168.30,
    "INTC":   30.15,
}

OUTPUT_DIR: str = "output"


class StockHolding:
    """Represents a single stock position in the portfolio.

    Attributes:
        ticker: The stock ticker symbol.
        quantity: Number of shares held.
        price: Price per share in USD.
        value: Total position value (auto-computed).
    """

    def __init__(self, ticker: str, quantity: int, price: float) -> None:
        """Initialize a StockHolding with auto-computed value.

        Args:
            ticker: Stock ticker symbol.
            quantity: Number of shares.
            price: Price per share in USD.
        """
        self.ticker: str = ticker
        self.quantity: int = quantity
        self.price: float = price
        self.value: float = quantity * price

    def __repr__(self) -> str:
        """Return a developer-friendly string representation."""
        return f"StockHolding({self.ticker}, qty={self.quantity}, value=${self.value:.2f})"


def print_available_stocks() -> None:
    """Display all available stocks and their prices."""
    print("\n Available Stocks:")
    print(" " + "-" * 30)
    for ticker, price in STOCK_PRICES.items():
        print(f"  {ticker:<6}  ${price:.2f}")
    print()


def get_ticker() -> str | None:
    """Prompt the user for a valid stock ticker.

    Returns:
        A valid ticker string, or None if the user types DONE.
        Returns empty string if ticker is invalid.
    """
    ticker: str = input(" Stock ticker (or DONE): ").upper().strip()

    if ticker == "DONE":
        return None

    if ticker not in STOCK_PRICES:
        print(f" '{ticker}' not found. Choose from: {list(STOCK_PRICES.keys())}")
        return ""

    return ticker


def get_quantity(ticker: str) -> int | None:
    """Prompt the user for a valid share quantity.

    Args:
        ticker: The stock ticker being purchased.

    Returns:
        A positive integer, or None if input is invalid.
    """
    quantity_input: str = input(f" How many shares of {ticker}? ").strip()

    if not quantity_input.isdigit() or int(quantity_input) <= 0:
        print(" Please enter a positive number.")
        return None

    return int(quantity_input)


def build_portfolio() -> list[StockHolding]:
    """Interactively build a portfolio from user input.

    Returns:
        A list of StockHolding objects.
    """
    portfolio: list[StockHolding] = []
    added_tickers: set[str] = set()

    print(" Enter your stocks. Type DONE when finished.\n")

    while True:
        ticker: str | None = get_ticker()

        if ticker is None:
            if len(portfolio) == 0:
                print(" Please add at least one stock.")
                continue
            break

        if ticker == "":
            continue

        if ticker in added_tickers:
            print(f" '{ticker}' already added.")
            continue

        quantity: int | None = get_quantity(ticker)
        if quantity is None:
            continue

        holding: StockHolding = StockHolding(ticker, quantity, STOCK_PRICES[ticker])
        portfolio.append(holding)
        added_tickers.add(ticker)
        print(f" Added: {quantity} x {ticker} = ${holding.value:.2f}\n")

    return portfolio


def print_portfolio_table(portfolio: list[StockHolding]) -> float:
    """Display the portfolio as a formatted table with weights.

    Args:
        portfolio: List of StockHolding objects.

    Returns:
        The total portfolio value.
    """
    total: float = sum(h.value for h in portfolio)

    print("\n" + "=" * 58)
    print(" YOUR PORTFOLIO")
    print("=" * 58)
    print(f" {'#':<4} {'Ticker':<8} {'Qty':>5} {'Price (USD)':>12} {'Value (USD)':>13} {'Weight':>7}")
    print(" " + "-" * 53)

    for i, h in enumerate(portfolio, 1):
        weight: float = (h.value / total * 100) if total > 0 else 0
        print(f" {i:<4} {h.ticker:<8} {h.quantity:>5} ${h.price:>10.2f} ${h.value:>11.2f} {weight:>6.1f}%")

    print(" " + "-" * 53)
    print(f" {'TOTAL':<4} {'':8} {'':>5} {'':>12} ${total:>11.2f} {'100.0%':>7}")
    print("=" * 58)
    print(f"\n Total Portfolio Value: ${total:,.2f}")

    return total


def export_to_csv(portfolio: list[StockHolding], total: float) -> None:
    """Export the portfolio to a timestamped CSV file.

    Args:
        portfolio: List of StockHolding objects.
        total: Total portfolio value.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filepath: str = os.path.join(OUTPUT_DIR, "portfolio_report.csv")

    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Generated", timestamp])
        writer.writerow([])
        writer.writerow(["Ticker", "Quantity", "Price (USD)", "Value (USD)", "Weight (%)"])

        for h in portfolio:
            weight: float = (h.value / total * 100) if total > 0 else 0
            writer.writerow([h.ticker, h.quantity, f"{h.price:.2f}", f"{h.value:.2f}", f"{weight:.2f}"])

        writer.writerow([])
        writer.writerow(["TOTAL", "", "", f"{total:.2f}", "100.00"])

    print(f" CSV saved to {filepath}")


def export_to_txt(portfolio: list[StockHolding], total: float) -> None:
    """Export the portfolio to a timestamped TXT file.

    Args:
        portfolio: List of StockHolding objects.
        total: Total portfolio value.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filepath: str = os.path.join(OUTPUT_DIR, "portfolio_report.txt")

    with open(filepath, "w") as f:
        f.write("STOCK PORTFOLIO REPORT\n")
        f.write(f"Generated: {timestamp}\n")
        f.write("=" * 50 + "\n\n")

        for h in portfolio:
            weight: float = (h.value / total * 100) if total > 0 else 0
            f.write(f"{h.ticker}: {h.quantity} shares x ${h.price:.2f} = ${h.value:.2f} ({weight:.1f}%)\n")

        f.write("\n" + "=" * 50 + "\n")
        f.write(f"TOTAL: ${total:,.2f}\n")

    print(f" TXT saved to {filepath}")


def main() -> None:
    """Entry point: runs the Stock Portfolio Tracker."""
    print("\n STOCK PORTFOLIO TRACKER")
    print(" CodeAlpha Python Internship — Task 2\n")

    print_available_stocks()
    portfolio: list[StockHolding] = build_portfolio()
    total: float = print_portfolio_table(portfolio)

    save: str = input("\n Save report to file? (y/n): ").lower().strip()
    if save == "y":
        export_to_csv(portfolio, total)
        export_to_txt(portfolio, total)

    print("\n Thank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Interrupted. Goodbye!")
