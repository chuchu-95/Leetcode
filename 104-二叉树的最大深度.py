# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.countDepth(root, 0)
    def countDepth(self, root, depth):
        if root == None:
            return depth
        depth = max(self.countDepth(root.left, depth+1), self.countDepth(root.right, depth+1))
        return depth