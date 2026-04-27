class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = [1] * len(nums)
        before_product = 1
        postfix = [1] * len(nums)
        after_product = 1
        for i in range(len(nums)): 
            prefix[i] *= before_product
            before_product *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1): 
            postfix[i] *= after_product
            after_product *= nums[i]
        
        for i in range(len(nums)): 
            result[i] *= prefix[i] * postfix[i]
        
        return result