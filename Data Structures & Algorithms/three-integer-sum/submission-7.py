class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)): 
            if i > 0: 
                if nums[i] == nums[i - 1]: 
                    continue
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2: 
                if nums[p1] + nums[p2] + nums[i] == 0: 
                    subresult = []
                    subresult.append(nums[i])
                    subresult.append(nums[p1])
                    subresult.append(nums[p2])
                    result.append(subresult)
                    temp = nums[p1]
                    while nums[p1] == temp and p1 < p2: 
                        p1 += 1


                elif nums[p1] + nums[p2] + nums[i] < 0: 
                    p1 += 1
                else: 
                    p2 -= 1
        return result