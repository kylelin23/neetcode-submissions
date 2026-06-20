class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        current = 1
        # Products on the left
        for i in range(len(nums)): 
            result[i] *= current
            current *= nums[i]
        
        current = 1
        # Products on the right
        for i in range(len(nums) - 1, -1, -1): 
            result[i] *= current
            current *= nums[i]
        
        return(result)