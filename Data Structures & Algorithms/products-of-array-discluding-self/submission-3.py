class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        temp = 1
        for i in range(len(nums)): 
            result[i] *= temp
            temp *= nums[i]
        
        temp = 1
        for i in range(len(nums) - 1, -1, -1): 
            result[i] *= temp
            temp *= nums[i]        
        
        return result