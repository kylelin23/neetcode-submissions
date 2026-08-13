class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */



    numIslands(grid: string[][]): number {

        function dfs(i: number, j: number): undefined {
            // Takes in a position on the grid
            // Checks if the position is valid and land
            // If not it terminates, otherwise it searches for more land to mark as visited
            if(i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] == '0'){
                return;
            }
            grid[i][j] = '0';
            dfs(i + 1, j);
            dfs(i, j + 1);
            dfs(i -1, j);
            dfs(i, j - 1);
        }

        let islandCount = 0;

        // Iterate through each node on grid
        for(let i = 0; i < grid.length; i++){
            for(let j = 0; j < grid[0].length; j++){
                // Increment island count by one
                if(grid[i][j] == '1'){
                    islandCount += 1;
                    // Run DFS on it
                    dfs(i, j);
                }
            }
        }
        // Return island count
        return islandCount;
    }
    
}
