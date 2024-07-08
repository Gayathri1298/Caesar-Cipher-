
def minimize_loss(prices):
    min_loss = float('inf')
    buy_year = -1
    sell_year = -1

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]: 
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss
                    buy_year = i + 1
                    sell_year = j + 1
    
    return buy_year, sell_year, min_loss

# Example 
prices = [20, 15, 7, 2, 13]
buy_year, sell_year, loss = minimize_loss(prices)
print(f"Buy in year {buy_year}, sell in year {sell_year}, with a loss of {loss}")