class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        result = []
        temp = 1
        for num in nums: 
            left.append(temp)
            temp *= num
        
        temp = 1
        for i in range(len(nums) - 1, -1, -1): 
            right.append(temp)
            temp *= nums[i]
        right = right[::-1]
        
        for i in range(len(nums)): 
            result.append(left[i] * right[i])
        
        return result