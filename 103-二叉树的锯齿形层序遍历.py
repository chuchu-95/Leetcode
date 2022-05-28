# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         result = []
#         if root == None:
#             return result
#         direct = True
#         queue = []
#         queue.append(root)
#         while queue:
#             sub = []
#             for i in range(len(queue)):
#                 rt = queue.pop(0)
#                 if direct:
#                     sub.append(rt.val)
#                 else:
#                     sub.insert(0, rt.val)
#                 if rt.left:
#                     queue.append(rt.left)
#                 if rt.right:
#                     queue.append(rt.right)
#             direct = not direct
#             result.append(sub)
#         return result

# 2022/4/25 deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        res = []
        if not root:
            return res
        queue = [root]
        judge = 1
        while queue:
            n = len(queue)
            temp = []
            sub = deque([], n)
            for i in range(n):
                node = queue[i]
                if judge == 1:
                    sub.append(node.val)
                elif judge == -1:
                    sub.appendleft(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(list(sub))
            queue = temp
            judge *= -1
        return res