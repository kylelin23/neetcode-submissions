class Solution {
    /**
     * @param {number[][]} grid
     */
    islandsAndTreasure(grid: number[][]): void {
        // Declare queue
        let queue : number[][] = [];
        let queueHead : number = 0;
        let directions : number[][] = [
            [0, 1], 
            [1, 0], 
            [0, -1], 
            [-1, 0]
        ];

        // Traverse through all nodes
        for(let i = 0; i < grid.length; i++){
            for(let j = 0; j < grid[0].length; j++){
                // If node is treasure
                if(grid[i][j] === 0){
                    // Enqueue node
                    queue.push([i, j]);
                }
            }
        }

        // While the queue is not empty
        while(queueHead < queue.length){
            // Pop out the first node
            let node = queue[queueHead];
            queueHead++;
            // For each neighbor
            for(let d of directions){
                // If its land and still INF (not visited yet)
                if(node[0] + d[0] >= 0 && node[1] + d[1] >= 0 && node[0] + d[0] < grid.length && node[1] + d[1] < grid[0].length && grid[node[0] + d[0]][node[1] + d[1]] === 2147483647){
                    // Make the value equal to current node's value + 1
                    grid[node[0] + d[0]][node[1] + d[1]] = grid[node[0]][node[1]] + 1;
                    // Enqueue the node
                    queue.push([node[0] + d[0], node[1] + d[1]]);
                }
            }
        }
    }
}
