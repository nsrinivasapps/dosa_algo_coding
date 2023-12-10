def cut_rod_max_profit(prices):
    n=len(prices)
    if n<=0:
        return 0
    dp=[0]*(n+1)
    
    for i in range(1,n+1):
        dp[i]=prices[i-1]
        for j in range(i):
            dp[i]=max(dp[i],dp[j]+dp[i-j])
    return dp[n]


if __name__ == "__main__":
    prices=[1,5,8,9,10,17,17,20]
    print(cut_rod_max_profit(prices))