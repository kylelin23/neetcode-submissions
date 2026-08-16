class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        // Initialize result array
        let result = [];
        // Sort nums
        nums = nums.sort((a, b) => a - b);
        console.log(nums)
        let p1 = 0;
        // Iterate through nums until second to last number is reached
        while(p1 < nums.length - 2){
            // To avoid duplicates
            // While it's not the first number and equal to prev number and not at second to last number: 
            while(p1 != 0 && nums[p1] == nums[p1 - 1] && p1 < nums.length - 2){
                p1 += 1;
            }
            // Implement two sum: 
            // While p2 is less than p3: 
            let p2 = p1 + 1;
            let p3 = nums.length - 1;
            while(p2 < p3)
                // If sum of all three is equal to zero: 
                if(nums[p1] + nums[p2] + nums[p3] == 0){
                    // Add to result
                    result.push(new Array([nums[p1], nums[p2], nums[p3]]));
                    // Increment p2 until non duplicate is reached
                    p2 += 1;
                    while(nums[p2] == nums[p2 - 1] && p2 < p3){
                        p2 += 1;
                    }
                }
                // Else: 
                else{
                    if(nums[p1] + nums[p2] + nums[p3] < 0){
                        p2 += 1;
                    }
                    else{
                        p3 -= 1;
                    }
                }
            // Increment p1
            p1 += 1;
        }

        return result;


    }
}
