class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)): 
            needed = target - nums[i]
            if needed in seen: 
                result = []
                result.append(seen[needed])
                result.append(i)
                return result
            else: 
                seen[nums[i]] = i
