class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        let seen = new Map();
        let result = [];
        for(let i = 0; i < nums.length; i++){
            if(seen.has(target - nums[i])){
                result.push(seen.get(target - nums[i]));
                result.push(i);
                return result;
            }
            seen.set(nums[i], i);
        }
    }
}
