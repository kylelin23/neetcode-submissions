class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        let result = new Array(nums.length).fill(1);
        let leftTotal = 1;
        for (let i = 0; i < nums.length; i++){
            result[i] *= leftTotal;
            leftTotal *= nums[i];
        }
        let rightTotal = 1;
        for (let i = nums.length - 1; i >= 0; i--){
            result[i] *= rightTotal;
            rightTotal *= nums[i];
        }
        return result;
    }
}
