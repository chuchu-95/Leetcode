# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = []
        stack = []
        flag = True
        point = None
        stack.append(root)
        while stack:
            curNode = stack[-1]
            while curNode:
                stack.append(curNode.left)
                curNode = curNode.left
            stack.pop()  # pop the last None root
            while stack:
                judgeNode = stack[-1]
                # judge if this node is a single root or it's right node have been append
                if judgeNode.right == None or judgeNode.right == point:
                    res.append(judgeNode.val)
                    stack.pop()
                    flag = True
                    point = judgeNode
                else:
                    stack.append(judgeNode.right)
                    flag = False
                
                if not flag:
                    break
        return res 