# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        rootBoundary = []
        if not root:
            return rootBoundary
        rootBoundary.append(root.val)
        if not root.left and not root.right:
            return rootBoundary
        leftBoundary = self.getLeftBoundary(root.left)
        leaves = self.getLeaves(root)
        rightBoundary = self.getRightBoundary(root.right)
        return rootBoundary + leftBoundary + leaves + rightBoundary

    def getLeftBoundary(self, node):
        res = []
        if not node:
            return res
        res.append(node.val)
        while node.left or node.right:
            if node.left:
                res.append(node.left.val)
                node = node.left
            else:
                if node.right:
                    res.append(node.right.val)
                    node = node.right
        res.pop()
        return res

    def getRightBoundary(self, node):
        res = []
        if not node:
            return res
        res.append(node.val)
        while node.left or node.right:
            if node.right:
                res.append(node.right.val)
                node = node.right
            else:
                if node.left:
                    res.append(node.left.val)
                    node = node.left
        res.pop()
        return res[::-1]

    def getLeaves(self, root):
        res = []
        def dfs(root):
            if not root:
                return 
            if not root.left and not root.right:
                res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res 

