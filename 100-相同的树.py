# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p != None and q != None:
            if p.val == q.val:
                if(self.isSameTree(p.left, q.left)):
                    if (self.isSameTree(p.right, q.right)):
                        return True
        return False