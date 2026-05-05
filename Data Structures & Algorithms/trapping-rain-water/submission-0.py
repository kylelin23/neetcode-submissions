class Solution:
    def trap(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        maxL = 0
        maxR = 0
        result = 0
        cur = p1
        while p1 < p2: 
            temp = min(maxL, maxR) - height[cur]
            if temp < 0: 
                temp = 0
            result += temp
            
            if height[p1] > maxL: 
                maxL = height[p1]
            if height[p2] > maxR: 
                maxR = height[p2]
            if height[p1] <= height[p2]: 
                p1 += 1
                cur = p1
            else: 
                p2 -= 1
                cur = p2
        return result