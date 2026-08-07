class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
        let start = 0;
        let end = 1;
        let result = 0;
        while (end < prices.length){
            let profit = prices[end] - prices[start];
            if (profit < 0){
                start = end;
            }
            else{
                result = Math.max(result, profit);
            }
            end += 1;
        }
        return result;
    }
}
