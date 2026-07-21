class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []
        for i in range(len(nums)): 
            if target - nums[i] in seen: 
                result.append(seen[target - nums[i]])
                result.append(i)
                return result
            seen[nums[i]] = i
        return