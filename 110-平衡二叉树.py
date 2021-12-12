# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        _, judge = self.judge(root)
        return judge
    
    def judge(self, root):
        # depth, judge
        if not root:
            return 0, True
        leftDepth, leftJudge = self.judge(root.left)
        rightDepth, rightJudge = self.judge(root.right)
        if leftJudge == False or rightJudge == False:
            return 0, False
        if abs(leftDepth - rightDepth) > 1:
            return 0,  False
        return max(leftDepth, rightDepth)+1, True


        