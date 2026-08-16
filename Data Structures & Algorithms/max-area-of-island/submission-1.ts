class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */


    maxAreaOfIsland(grid: number[][]): number {

        let result = 0;
        
        function dfs(i: number, j: number): number{
            if(i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] == 0){
                return 0;
            }
            grid[i][j] = 0;
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1);
        }

        for(let i = 0; i < grid.length; i++){
            for(let j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 1){
                    result = Math.max(result, dfs(i, j));
                }
            }
        }
        return result;
    }
    
}
