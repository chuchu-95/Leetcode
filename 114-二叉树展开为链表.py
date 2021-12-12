# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         preLst = []
#         self.preTraverse(root, preLst)
#         for idx in range(1, len(preLst)):
#             preNode = preLst[idx-1]
#             curNode = preLst[idx]
#             preNode.left = None
#             preNode.right = curNode
    
#     def preTraverse(self, root, preLst):
#         if root:
#             preLst.append(root)
#             self.preTraverse(root.left, preLst)
#             self.preTraverse(root.right, preLst)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return 
        reslst = []
        stack = []
        stack.append(root)
        preNode = TreeNode(0)
        while stack:
            curNode = stack.pop()
            preNode.left = None
            preNode.right = curNode
            l = curNode.left
            r = curNode.right
            if r:
                stack.append(r)
            if l:
                stack.append(l)
            preNode = curNode

            
