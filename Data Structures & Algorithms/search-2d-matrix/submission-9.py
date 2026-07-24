class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary Search to find correct row
        top = 0
        bottom = len(matrix) - 1
        targetRow = None
        while top <= bottom: 
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                targetRow = mid
                break
            elif matrix[mid][0] > target: 
                bottom = mid - 1
            else: 
                top = mid + 1
        print(targetRow)

        if targetRow != None: 
            l = 0
            r = len(matrix[targetRow]) - 1
            while l <= r: 
                mid = (l + r) // 2
                if matrix[targetRow][mid] == target: 
                    return True
                elif matrix[targetRow][mid] < target: 
                    l = mid + 1
                else: 
                    r = mid - 1
        return False