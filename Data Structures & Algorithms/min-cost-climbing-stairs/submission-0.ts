class Solution {
    /**
     * @param {number[]} cost
     * @return {number}
     */
    minCostClimbingStairs(cost: number[]): number {
        let first = cost[cost.length - 2];
        let second = cost[cost.length - 1];
        let temp;

        for(let i = cost.length - 3; i >= 0; i--){
            temp = first;
            first = cost[i] + Math.min(first, second)
            second = temp;
        }
        return Math.min(first, second);
    }
}
