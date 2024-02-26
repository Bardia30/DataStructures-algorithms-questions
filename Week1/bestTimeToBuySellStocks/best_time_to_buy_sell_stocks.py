def maxProfit(prices):
    max_profit = 0

    buy= 0
    sell = 1

    while sell < len(prices):
        profit = prices[sell] - prices[buy]
        
        if profit < 0:
            buy = sell
        if profit > max_profit:
            max_profit = profit
            
        sell += 1
    return max_profit


print(maxProfit([2,1,4]))

