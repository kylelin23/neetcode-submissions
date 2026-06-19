class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        result = []
        for num in nums: 
            if num in counts: 
                counts[num] += 1
            else: 
                counts[num] = 1
        
        freq = [[] for i in range(len(nums))]
        for count in counts.keys(): 
            freq[counts[count] - 1].append(count)
        
        for i in range(len(freq) - 1, -1, -1): 
            for j in freq[i]: 
                result.append(j)
                k -= 1
                if k == 0: 
                    return result