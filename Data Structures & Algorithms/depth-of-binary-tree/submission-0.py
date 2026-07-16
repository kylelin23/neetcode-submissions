# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        leftDepth = 0
        rightDepth = 0
        if root == None: 
            return 0
        if root.left or root.right: 
            leftDepth = 1 + self.maxDepth(root.left)
            rightDepth = 1 + self.maxDepth(root.right)
        else: 
            # One Node
            return 1
        return max(leftDepth, rightDepth)