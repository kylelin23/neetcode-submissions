class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights: number[]): number {
        let p1 = 0;
        let p2 = heights.length - 1;
        let result = 0;
        // Iterate two pointers
        while(p1 < p2){
            // Calculate area
            // Update result
            result = Math.max(result, Math.min(heights[p1], heights[p2]) * (p2 - p1));
            // Increment pointers
            if(heights[p1] > heights[p2]){
                p2 -= 1;
            }
            else{
                p1 += 1;
            }
        }
        return result;
    }
}
