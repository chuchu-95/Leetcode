# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         return self.judge(root, root)
#     def judge(self, p, q):
#         if p == None and q == None:
#             return True
#         if p == None or q == None:
#             return False
#         else:
#             if p.val == q.val:
#                 return (self.judge(p.left, q.right)) and (self.judge(p.right, q.left))
#         return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]
        while queue:
            lt = queue.pop(0)
            rt = queue.pop(0)
            if lt == None and rt == None:
                continue
            if (lt == None or rt == None) or lt.val != rt.val:
                return False
            else:
                queue.append(lt.left)
                queue.append(rt.right)
                queue.append(lt.right)
                queue.append(rt.left)
        return True
                
        
