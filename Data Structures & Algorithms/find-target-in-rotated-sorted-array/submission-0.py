class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # Find Pivot
        while l <= r: 
            mid = (l + r) // 2
            if nums[mid] < nums[0]: # In rotated part
                r = mid - 1
            else: 
                l = mid + 1
        pivot = l

        # Binary Search Algorithm
        def b_s(n, target): 
            l = 0
            r = len(n) - 1
            while l <= r: 
                mid = (l + r) // 2
                if n[mid] == target: 
                    return mid
                elif n[mid] > target: 
                    r = mid - 1
                else: 
                    l = mid + 1
            return -1
        # Perform Binary Search on both sorted arrays
        array1 = nums[0:pivot]
        array2 = nums[l:]
        print(array1)
        print(array2)
        print(target)
        array1Result = b_s(array1, target)
        if array1Result >= 0: 
            return array1Result
        else: 
            array2Result = b_s(array2, target)
            if array2Result >= 0:
                return array2Result + len(array1)
            else: 
                return -1