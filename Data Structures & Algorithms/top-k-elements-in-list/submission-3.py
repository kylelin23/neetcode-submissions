class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums: 
            if num in counts: 
                counts[num] += 1
            else: 
                counts[num] = 1
        
        sorting = [[] for i in range(len(nums) + 1)]
        for count in counts: 
            sorting[counts[count]].append(count)
        
        result = []
        for i in range(len(sorting) - 1, 0, -1): 
            for num in sorting[i]: 
                if k <= 0: 
                    return result
                else: 
                    result.append(num)
                    k -= 1
        return(result)