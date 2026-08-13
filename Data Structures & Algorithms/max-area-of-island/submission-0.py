class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # define result
        result = 0

        # DFS helper function
        # Returns area of island
        def dfs(i, j): 
            # Check if island is invalid or water (base case)
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0: 
                # If not, return 0
                return 0
            # mark current node as visited
            grid[i][j] = 0
            # return the sum of dfs of all directions
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        # Iterate through all nodes in grid
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                # do dfs on current node and update result
                result = max(result, dfs(i, j))
        
        return result