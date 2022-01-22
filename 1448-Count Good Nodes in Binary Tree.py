# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num = 0
        def count(root, curMax):
            if not root:
                return 
            nonlocal num
            if root.val >= curMax:
                num += 1
            count(root.left, max(root.val, curMax))
            count(root.right, max(root.val, curMax))
        count(root, root.val)
        return num
