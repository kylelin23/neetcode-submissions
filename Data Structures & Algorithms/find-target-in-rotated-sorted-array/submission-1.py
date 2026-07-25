class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r: 
            mid = (l + r) // 2
            if nums[mid] < nums[0]: 
                r = mid - 1
            else: 
                l = mid + 1
        
        def binary_search(numbers, target): 
            l = 0
            r = len(numbers) - 1
            while l <= r: 
                mid = (l + r) // 2
                if numbers[mid] == target: 
                    return mid
                elif numbers[mid] > target: 
                    r = mid - 1
                else: 
                    l = mid + 1
            return -1
        print(l)
        first_arr = nums[0:l]
        second_arr = nums[l:]
        print(first_arr)
        print(second_arr)
        result = binary_search(first_arr, target)
        print(result)
        if result != -1: 
            return result
        else: 
            result = binary_search(second_arr, target)
            print(result)
            if result != -1: 
                return result + len(first_arr)
            else: 
                return -1