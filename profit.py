def stock_profit(stock):

        prof = 0
        l = len(stock)
        
        for i in range(l - 1):
                for x in range(i + 1, l):
                        prof = max(prof, stock[x] - stock[i])
        return prof


print("Example:")
print(stock_profit([3, 1, 3, 4, 5, 1]))


print(stock_profit([2, 3, 4, 5]))
print(stock_profit([3, 1, 3, 4, 5, 1]))
print(stock_profit([4, 3, 2, 1]))
print(stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]))
print(stock_profit([1, 1, 1, 2, 1, 1, 1]))
print(stock_profit([4, 3, 2, 1, 2, 1, 2, 1]))
print(stock_profit([1, 1, 1, 1]))

print("You are the best broker here! Click 'Check' to earn cool rewards!")
