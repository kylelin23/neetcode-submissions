class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        maxVolume = 0
        while p1 < p2: 
            volume = min(heights[p1], heights[p2]) * (p2 - p1)
            if volume > maxVolume: 
                print(p1)
                print(p2)
                maxVolume = volume
            if heights[p1] > heights[p2]: 
                p2 -= 1
            else: 
                p1 += 1
        return maxVolume