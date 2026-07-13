class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = 0
        while l <= r: 
            mid = (l + r) // 2
            totalTime = 0
            for p in piles: 
                print("p: " + str(p))
                print("mid: " + str(mid))
                totalTime += math.ceil(p/mid)
                print(totalTime)
            if totalTime <= h: 
                result = mid
                r = mid - 1
            else: 
                l = mid + 1
        return result