# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = []
        queue.append(root)
        while queue:
            sub = []
            for i in range(len(queue)):
                value = queue.pop(0)
                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)
                sub.append(value.val)
            result.insert(0, sub)
        return result