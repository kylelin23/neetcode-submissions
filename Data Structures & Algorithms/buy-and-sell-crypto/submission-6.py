class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        maxProfit = 0
        while end < len(prices): 
            profit = prices[end] - prices[start]
            maxProfit = max(maxProfit, profit)
            if profit <= 0: 
                start = end
            end += 1
        return maxProfit