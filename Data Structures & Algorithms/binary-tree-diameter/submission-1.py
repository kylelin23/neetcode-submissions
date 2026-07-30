# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root): 
            nonlocal res
            if root == None: 
                return 0
            
            leftMaxHeight = dfs(root.left)
            rightMaxHeight = dfs(root.right)
            res = max(res, leftMaxHeight + rightMaxHeight)
            return 1 + max(leftMaxHeight, rightMaxHeight)
        dfs(root)
        return res