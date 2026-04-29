class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = []
        result = 0
        nums = set(nums)
        for num in nums: 
            if num - 1 not in nums: 
                seq.append(num)
                # Start of sequence
                while num + 1 in nums: 
                    seq.append(num + 1)
                    num += 1
                if len(seq) > result: 
                    result = len(seq)
                seq = []
        return result