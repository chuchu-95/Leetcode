# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def recursion(node):
            if not node:
                return None
            if not node.left and not node.right:
                sub.append(node.val)
                return None
            node.left = recursion(node.left)
            node.right = recursion(node.right)
            return node

        leaves = []
        while root:
            sub = []
            root = recursion(root)
            leaves.append(sub)
        return leaves