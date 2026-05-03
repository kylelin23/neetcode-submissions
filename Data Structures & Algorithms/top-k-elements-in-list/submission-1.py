class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = {}
        for num in nums: 
            if num in counts: 
                counts[num] += 1
            else: 
                counts[num] = 1
        print(counts)
        
        freq = [[] for i in range(len(nums) + 1)]
        for i in counts.keys(): 
            freq[counts[i]].append(i)

        print(freq)
        for i in range(len(freq) - 1, -1 , -1):
            if k == 0: 
                return result
            for num in freq[i]: 
                result.append(num)
                k -= 1