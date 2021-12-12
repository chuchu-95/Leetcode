# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        self.sum = 0 
        # dfs
        def dfs(root, sub):
            if not root.left and not root.right:
                self.sum += (sub*10+root.val)
            else:
                if root.left:
                    dfs(root.left, sub*10+root.val)
                if root.right:
                    dfs(root.right, sub*10+root.val)
        dfs(root, 0)
        return self.sum