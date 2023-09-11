class Solution(object):
    def maxProfit(self, prices):
        minimum = min(prices)
        min_in = prices.index(minimum)
        if min_in+1 == len(prices):
            return "You've run out of days to sell the stock !"
        i = 1
        while i < min_in+1:
            prices.pop(i-1)
            i+=1
        return f"You can buy stock on day {min_in+1} and sell it on day {(i-1)+prices.index(max(prices))+1} to gain maxProfit !"
    
prices = [5,3,4,5,1,6,7]
sol = Solution()
print(sol.maxProfit(prices))