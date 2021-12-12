# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.helper(inorder, postorder)
    def helper(self, inorder, postorder):
        if len(inorder) == 0  and len(postorder) == 0:
            return None
        root = TreeNode(postorder.pop())
        idx = 0
        while idx < len(inorder):
            if inorder[idx] == root.val:
                break
            idx += 1
        root.left = self.helper(inorder[0:idx], postorder[0:idx])
        root.right = self.helper(inorder[idx+1:], postorder[idx:])
        return root