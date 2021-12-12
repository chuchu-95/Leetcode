# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.helper(root, 1)
    def helper(self, root, depth):
        if root.left == None and root.right == None:
            return depth
        if root.left == None and root.right:
            return self.helper(root.right, depth+1)
        if root.left and root.right == None:
            return self.helper(root.left, depth+1)
        leftDepth = self.helper(root.left, depth+1)
        rightDepth = self.helper(root.right, depth+1)
        return min(leftDepth, rightDepth)
                