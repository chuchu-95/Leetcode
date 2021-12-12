# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def recoverTree(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         inTree = self.inRootTraverse(root, [])
#         change1 = None
#         change2 = None
#         judge = False
#         for idx in range(len(inTree)-1):
#             if inTree[idx].val > inTree[idx+1].val:
#                 change2 = inTree[idx+1]
#                 if change1 == None:
#                     change1 = inTree[idx]
#         #exchange
#         if change1 != None and change2 != None:
#             a = change1.val 
#             change1.val = change2.val
#             change2.val = a
#     def inRootTraverse(self, rt, res):
#         if rt != None:
#             self.inRootTraverse(rt.left, res)
#             res.append(rt)
#             self.inRootTraverse(rt.right, res)
#         return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.ch1 = None
        self.ch2 = None
        self.pre = None
        def inTreeTraverse(rt):
            if rt != None:
                inTreeTraverse(rt.left)
                if self.pre == None:
                    self.pre = rt
                else:
                    if self.pre.val > rt.val:
                        self.ch2 = rt
                        if not self.ch1:
                            self.ch1 = self.pre
                    self.pre = rt
                inTreeTraverse(rt.right)
        inTreeTraverse(root)
        if self.ch1 and self.ch2:
            a = self.ch1.val
            self.ch1.val = self.ch2.val
            self.ch2.val = a
    

