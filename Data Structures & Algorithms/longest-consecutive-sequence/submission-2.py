class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxResult = 0
        for num in nums: 
            result = 0
            if (num - 1) not in nums: 
                # start of sequence
                result += 1
                cur = num
                while (cur + 1) in nums: 
                    cur += 1
                    result += 1
            if result > maxResult: 
                maxResult = result
        return maxResult