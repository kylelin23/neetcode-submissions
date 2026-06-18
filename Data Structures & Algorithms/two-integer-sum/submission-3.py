class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # key: num, value: index
        result = []
        for i in range(len(nums)): 
            if target - nums[i] in seen.keys(): 
                result.append(seen[target - nums[i]])
                result.append(i)
                return result
            seen[nums[i]] = i