class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n: number): number {
        let first = 1; // N-1th step
        let second = 1; // Nth step
        for(let i = 0; i < n - 1; i++){
            let temp = first;
            first += second;
            second = temp;
        }
        return first;
    }
}
