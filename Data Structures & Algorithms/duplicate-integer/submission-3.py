class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy = nums
        nums = set(nums)
        return(len(copy) != len(nums))