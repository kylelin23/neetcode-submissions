class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights: number[]): number {
        let p1 = 0;
        let p2 = heights.length - 1;
        let result = 0;
        while(p1 < p2){
            let area = Math.min(heights[p1], heights[p2]) * (p2 - p1);
            result = Math.max(result, area);
            if (heights[p1] > heights[p2]){
                p2 -= 1
            }
            else{
                p1 += 1
            }
        }
        return result;
    }
}
