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
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
        if(root == null && subRoot == null){
            return true;
        }
        else if(root == null || subRoot == null){
            return false;
        }
        else{
            return (this.isSameTree(root, subRoot) || this.isSubtree(root.left, subRoot) || this.isSubtree(root.right, subRoot))
        }
    }
    isSameTree(p: TreeNode | null, q: TreeNode | null): boolean{
        if(p == null && q == null){
            return true
        }
        else if(p == null || q == null){
            return false
        }
        else{
            if (p.val != q.val){
                return false
            }
            else{
                return this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right)
            }
        }
    }
}
