# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.move = 0
        self.dfs(root)
        return self.move
    def dfs(self, root):
        if not root:
            return 0
        leftMove = self.dfs(root.left)
        rightMove = self.dfs(root.right)
        self.move += abs(leftMove) + abs(rightMove)
        return root.val-1 + leftMove + rightMove