class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxResult = 0
        for num in nums: 
            result = 0
            if (num - 1) not in nums: # Start of sequence
                temp = num
                while temp in nums: 
                    result += 1
                    temp += 1
            maxResult = max(maxResult, result)
        return maxResult