# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) :
        result = []
        if root == None:
            return result
        sub = []
        queue = [] 
        queue.append(root)
        while queue:
            sub = []
            for i in range(len(queue)):
                rt = queue.pop(0)
                sub.append(rt.val)
                if rt.left:
                    queue.append(rt.left)
                if rt.right:
                    queue.append(rt.right)
            result.append(sub)
        return result