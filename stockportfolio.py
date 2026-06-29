stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 320
}

def show_available_stocks():
    print("\n" + "=" * 40)
    print("       Available Stocks")
    print("=" * 40)
    for stock, price in stock_prices.items():
        print(f"  {stock} — ${price} per share")
    print("=" * 40)

def calculate_portfolio():
    portfolio = {}
    total = 0

    print("=" * 40)
    print("   Welcome to Stock Portfolio Tracker")
    print("=" * 40)

    show_available_stocks()

    while True:
        stock = input("\nEnter stock name (or 'done' to finish): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not found! Please choose from the list above.")
            continue

        quantity = input(f"Enter quantity of {stock} shares: ").strip()

        if not quantity.isdigit() or int(quantity) <= 0:
            print("❌ Please enter a valid quantity!")
            continue

        quantity = int(quantity)
        portfolio[stock] = portfolio.get(stock, 0) + quantity

    if not portfolio:
        print("\n⚠️  No stocks added!")
        return

    print("\n" + "=" * 40)
    print("       Your Portfolio Summary")
    print("=" * 40)
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        total += value
        print(f"  {stock}: {quantity} shares x ${stock_prices[stock]} = ${value}")

    print("=" * 40)
    print(f"  Total Investment: ${total}")
    print("=" * 40)

calculate_portfolio()