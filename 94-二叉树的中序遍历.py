# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         #left - root - right
#         res = []
#         def dfs(root):
#             if root != None:
#                 dfs(root.left)
#                 res.append(root.val)
#                 dfs(root.right)
#         dfs(root)
#         return res
