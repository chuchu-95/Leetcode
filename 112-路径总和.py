# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum)
    def helper(self, root, targetSum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return targetSum == root.val     
        leftJudge = self.helper(root.left, targetSum-root.val)
        if leftJudge:
            return True
        rightJudge = self.helper(root.right, targetSum-root.val)
        return leftJudge or rightJudge