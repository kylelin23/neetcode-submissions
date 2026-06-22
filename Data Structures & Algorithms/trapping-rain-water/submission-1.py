class Solution:
    def trap(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        max_left = height[p1]
        max_right = height[p2]
        result = 0
        while p1 < p2: 
            if height[p1] < height[p2]: 
                p1 += 1
                max_left = max(max_left, height[p1])
                result += max(0, min(max_left, max_right) - height[p1])
            else: 
                p2 -= 1
                max_right = max(max_right, height[p2])
                result += max(0, min(max_left, max_right) - height[p2])
        return result