"""
in this exercise check for the best buy for and best sell and get maximum profit
    ex: input = [7,1,2,4,6,3]
        output = [1,4]
"""

prices = [7,2,1,4,6,3]

def best_time_buy_sell(arr):
    max_profit = 0
    min_price = arr[0]
    buy = 0
    best_sell = 0
    best_buy = 0

    for i in range(len(arr) - 1):
        if arr[i] < min_price:
            min_price = arr[i]
            buy = i
        else:
            profit = arr[i] - min_price
            if profit > max_profit:
                max_profit = profit
                best_buy = buy
                best_sell = i
    print(f"the max profit from the given prices is {max_profit} with indices {best_buy} and {best_sell}")

best_time_buy_sell(prices)
