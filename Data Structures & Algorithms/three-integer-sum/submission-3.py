class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)): 
            if i != 0 and nums[i - 1] == nums[i]: 
                continue
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2: 
                threeSum = nums[i] + nums[p1] + nums[p2]
                if threeSum > 0: 
                    p2 -= 1
                elif threeSum < 0: 
                    p1 += 1
                else: 
                    temp = []
                    temp.append(nums[i])
                    temp.append(nums[p1])
                    temp.append(nums[p2])
                    result.append(temp)
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and nums[p1] == nums[p1 - 1]: 
                        p1 += 1
        return result
                