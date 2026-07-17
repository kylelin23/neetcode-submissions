# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def dfs(root): 
            nonlocal isBalanced
            if root == None: 
                return 0
            left = dfs(root.left) # 1
            right = dfs(root.right) # 3
            if abs(left - right) >= 2: 
                isBalanced = False
            return 1 + max(left, right)
        
        dfs(root)
        return isBalanced