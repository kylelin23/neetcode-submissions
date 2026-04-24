from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 10:20
        result = []
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums: 
            if num in counts: 
                counts[num] += 1
            else: 
                counts[num] = 1

        for num in counts.keys(): 
            freq[counts[num]].append(num)

        for i in range(len(freq) - 1, -1, -1): 
            for num in freq[i]: 
                result.append(num)
                k = k - 1
                if k == 0: 
                    return result