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
    diameterOfBinaryTree(root: TreeNode | null): number {
        let maxDiameter = 0;
        function dfs(root: TreeNode | null): number{
            if(root == null){
                return 0;
            }
            let leftMax = dfs(root.left);
            let rightMax = dfs(root.right);
            maxDiameter = Math.max(maxDiameter, leftMax + rightMax);
            return (1 + Math.max(leftMax, rightMax));
        }
        dfs(root);
        return maxDiameter;

    }
}
