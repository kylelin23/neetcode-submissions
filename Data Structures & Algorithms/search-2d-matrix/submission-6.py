class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1
        row = []
        while t <= b: 
            mid = (t + b) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]: 
                row = matrix[mid]
                print("fnwelfnew")
                break
            elif target > matrix[mid][-1]: 
                t = mid + 1
            else: 
                b = mid - 1
        if row == []: 
            return False
        print(row)
        l = 0
        r = len(matrix[0]) - 1
        while l <= r: 
            mid = (l + r) // 2
            if row[mid] == target: 
                return True
            elif row[mid] > target: 
                r = mid - 1
            else: 
                l = mid + 1
        return False
        