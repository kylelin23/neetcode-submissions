class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = start + 1
        result = 0
        while end < len(prices): 
            profit = prices[end] - prices[start]
            if profit > result: 
                result = profit
            if profit <= 0: 
                start = end
            end += 1
        return result