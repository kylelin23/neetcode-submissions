class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        p1 = 0
        seen = set()
        result = []
        while p1 < (len(nums) - 2): 
            while nums[p1] in seen and p1 < (len(nums) - 2): 
                p1 += 1

            p2 = p1 + 1
            p3 = len(nums) - 1
            while p2 < p3: 
                target = nums[p1] + nums[p2] + nums[p3]
                if target == 0: 
                    temp = []
                    temp.append(nums[p1])
                    temp.append(nums[p2])
                    temp.append(nums[p3])
                    result.append(temp)
                    p2 += 1
                    while nums[p2] == nums[p2 - 1] and p2 < p3: 
                        p2 += 1
                elif target > 0: 
                    p3 -= 1
                else: 
                    p2 += 1
            seen.add(nums[p1])
            p1 += 1
        return result