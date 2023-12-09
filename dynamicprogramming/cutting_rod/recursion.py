def cut_rod_max_profit(prices):
    def cut_rod_rec(n):
        if n <= 0:
            return 0
        
        maxValue = 0
        for i in range(n):
            maxValue = max(maxValue,prices[i]+cut_rod_rec(n-i-1))
        return maxValue

    n = len(prices)
    return cut_rod_rec(n)

if __name__ == "__main__":
    prices=[1,5,8,9,10,17,17,20]
    print(cut_rod_max_profit(prices))