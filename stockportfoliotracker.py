stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_value = 0

print("STOCK PORTFOLIO TRACKER")

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = quantity
    else:
        print("Stock not found!")

# Calculate total investment
print("\nPortfolio Summary:")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value = ${total_value}")

# Save to file
with open("portfolio_report.txt", "w") as file:
    file.write("Stock Portfolio Report\n")
    file.write("======================\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares = ${value}\n")

    file.write(f"\nTotal Investment Value = ${total_value}")

print("\nReport saved as portfolio_report.txt")
