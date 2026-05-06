class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        maxProfit = 0
        while end < len(prices): 
            print(start)
            print(end)
            profit = prices[end] - prices[start]
            if profit > maxProfit: 
                maxProfit = profit
            if profit <= 0: 
                start = end
            end += 1
        return maxProfit