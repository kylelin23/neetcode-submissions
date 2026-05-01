class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        result = []
        while p1 < p2: 
            print(numbers[p1] + numbers[p2])
            if numbers[p1] + numbers[p2] == target: 
                result.append(p1 + 1)
                result.append(p2 + 1)
                return result
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
            else: 
                p1 += 1
        