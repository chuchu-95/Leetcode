# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.helper(root, None, None)

    def helper(self, rt, min, max):
        if rt == None:
            return True
        if (min != None and rt.val <= min) or (max != None and rt.val >= max):
            return False
        leftJudge = self.helper(rt.left, min, rt.val)
        rightJudge = self.helper(rt.right, rt.val, max)
        return leftJudge and rightJudge
