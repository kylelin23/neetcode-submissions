/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxDepth(root: TreeNode | null): number {
        let maxDepth = 0;
        function dfs(root: TreeNode): number{
            if(root == null){
                return 0;
            }
            let leftMax = dfs(root.left);
            let rightMax = dfs(root.right);
            let temp = Math.max(leftMax, rightMax);
            maxDepth = Math.max(maxDepth, 1 + temp);
            return (1 + temp)
        }
        dfs(root);
        return maxDepth
    }
}
