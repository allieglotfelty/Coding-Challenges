stock_prices_yesterday = [10, 3, 7, 5, 8, 4, 9]

def get_max_profit(stock_prices):
    """Takes stock_prices_yesterday and returns the best profit I could have
    made from 1 purchase and 1 sale of 1 Apple stock yesterday."""

    # Find the biggest difference between two numbers where the smallest number
    # Comes first

    best_price = 0

    for i in range(len(stock_prices)):
        for j in stock_prices[i:]:
            price = j - stock_prices[i]
            print "%s - %s is %s" % (j, stock_prices[i], price)
            # print price
            best_price = max([best_price, price])

    return best_price

print get_max_profit(stock_prices_yesterday)
