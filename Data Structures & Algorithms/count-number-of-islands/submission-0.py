class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        # Marking node (i, j) and all connecting land as visited
        def dfs(i, j): 
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0': 
                return
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        
        for i in range(len(grid)): 
            for j in range((len(grid[0]))): 
                # For each node in the grid

                # If it is land mark it as an island and then mark all other connecting land
                if grid[i][j] == '1': 
                    islands += 1
                    dfs(int(i), int(j))
        return islands