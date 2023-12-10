def cut_rod_max_profit(prices):

    def cut_rod_rec(n):
        if n <= 0:##Base case when rod to cut length <= 0
            return 0
        if maxValueList[n-1] != 0:##get the previously calculated value
            return maxValueList[n-1]
        for i in range(n):##calculate if it is first time
            maxValueList[n-1] = max(maxValueList[n-1],prices[i]+cut_rod_rec(n-i-1))
        return maxValueList[n-1]
    
    n = len(prices)    
    maxValueList = [0]*n##initialize global array
    maxValueList[0] = prices[0]
    cut_rod_rec(n)
    return maxValueList[n-1]

if __name__ == "__main__":
    prices=[1,5,8,9,10,17,17,20]
    print(cut_rod_max_profit(prices))