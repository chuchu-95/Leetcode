# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.help(preorder, inorder)
    def help(self, preorder, inorder):
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        idx = 0
        while idx < len(inorder):
            if inorder[idx] == preorder[0]:
                break
            idx += 1
        root.left = self.help(preorder[1:idx+1], inorder[0:idx])
        root.right = self.help(preorder[idx+1:], inorder[idx+1:])
        return root
