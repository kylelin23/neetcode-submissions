class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        row = None
        while top <= bottom: 
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target: 
                row = mid
                break
            elif matrix[mid][0] > target: 
                bottom = mid - 1
            else: 
                top = mid + 1

        if row == None: 
            return False
        
        l = 0
        r = len(matrix[row]) - 1
        while l <= r: 
            mid = (l + r) // 2
            if target == matrix[row][mid]: 
                return True
            elif target > matrix[row][mid]: 
                l = mid + 1
            else: 
                r = mid - 1
        return False