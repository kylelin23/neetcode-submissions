class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = float('inf')
        while l <= r: 
            mid = (l + r) // 2
            totalTime = 0
            for p in piles: 
                totalTime += math.ceil(float(p) / float(mid))
            if totalTime <= h: 
                result = min(result, mid)
                r = mid - 1
            else: 
                l = mid + 1
        return result