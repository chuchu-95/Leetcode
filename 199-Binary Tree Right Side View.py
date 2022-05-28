# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dfs-recrusive
        # res = []
        # def dfs(root, level):
        #     if not root:
        #         return 
        #     if level == len(res):
        #         res.append(root.val)
        #     dfs(root.right, level+1)
        #     dfs(root.left, level+1)
        # dfs(root, 0)
        # return res

        # dfs-iteration
        # res = []
        # if not root:
        #     return res
        # stack = []
        # cnt = [0]
        # stack.append(root)
        # while stack:
        #     cur = stack.pop()
        #     n = cnt.pop()
        #     if len(res) == n:
        #         res.append(cur.val)
        #     if cur.left:
        #         cnt.append(n+1)
        #         stack.append(cur.left)
        #     if cur.right:
        #         cnt.append(n+1)
        #         stack.append(cur.right)
        # return res

        # bfs - the last element of each layer
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            n = len(queue)
            while n > 0:
                cur = queue.pop(0)
                n -= 1
                if n == 0:
                    res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res
