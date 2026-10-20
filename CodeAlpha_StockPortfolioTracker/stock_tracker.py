"""
CodeAlpha Python Internship - Task 2: Stock Portfolio Tracker
Author: Your Name
Description: Calculates the total value of a stock portfolio using
             hardcoded stock prices. The result can be saved to a
             text file.
"""

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}

OUTPUT_FILE = "portfolio_summary.txt"


def get_quantity(stock):
    """Ask for a valid non-negative whole number of shares."""
    while True:
        try:
            quantity = int(input(f"Quantity of {stock}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            return quantity
        except ValueError:
            print("Please enter a whole number.")


def collect_portfolio():
    """Let the user add stocks until they type 'done'. Returns {stock: quantity}."""
    portfolio = {}
    print("Available stocks:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print("Stock not found. Please choose from the list above.")
            continue
        quantity = get_quantity(stock)
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    return portfolio


def build_summary(portfolio):
    """Return (summary_text, total_investment) for the portfolio."""
    lines = ["Stock Portfolio Summary", "-" * 40]
    total = 0
    for stock, quantity in portfolio.items():
        value = STOCK_PRICES[stock] * quantity
        total += value
        lines.append(f"{stock:<6} {quantity:>5} x ${STOCK_PRICES[stock]:<6} = ${value:,}")
    lines.append("-" * 40)
    lines.append(f"Total investment: ${total:,}")
    return "\n".join(lines), total


def save_to_file(summary):
    """Write the summary to a text file."""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(summary + "\n")
    print(f"\nSummary saved to {OUTPUT_FILE}")


def main():
    print("=== Stock Portfolio Tracker ===")
    portfolio = collect_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    summary, _ = build_summary(portfolio)
    print("\n" + summary)

    if input("\nSave result to file? (yes/no): ").strip().lower() in ("yes", "y"):
        save_to_file(summary)


if __name__ == "__main__":
    main()
