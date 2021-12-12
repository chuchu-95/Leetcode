# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root == None:
            return result
        direct = True
        queue = []
        queue.append(root)
        while queue:
            sub = []
            for i in range(len(queue)):
                rt = queue.pop(0)
                if direct:
                    sub.append(rt.val)
                else:
                    sub.insert(0, rt.val)
                if rt.left:
                    queue.append(rt.left)
                if rt.right:
                    queue.append(rt.right)
            direct = not direct
            result.append(sub)
        return result