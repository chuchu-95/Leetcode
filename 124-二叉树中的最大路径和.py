# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def __init__(self, maxNum):
#         self.maxNum = maxNum

#     def maxPathSum(self, root):
#         # recursion
#         # root+left+right, root+left, root+right, root, left, right
#         def resur(root):
#             if root == None:
#                 return -1000-1
#             leftVal = resur(root.left)
#             print(root.val)
#             print("leftVal", leftVal)

#             rightVal = resur(root.right)
#             print("rightVal", rightVal)
#             self.maxNum = max(self.maxNum, root.val+leftVal+rightVal, leftVal, rightVal)
#             print("maxNum", self.maxNum)
#             return max(root.val, root.val+leftVal, root.val+rightVal)
        
#         res = resur(root)
#         print(max(self.maxNum, res))
#         return max(self.maxNum, res)

# root = TreeNode(1)
# a = TreeNode(-2)
# b = TreeNode(-3)
# root.left = a
# root.right = b
# c = TreeNode(1)
# d = TreeNode(3)
# a.left = c
# a.right = d
# e = TreeNode(-2)
# b.left = e
# c.left = TreeNode(-1)
# s = Solution(-1001)
# print(s.maxPathSum(root))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # recursion
        # root+left+right, root+left, root+right, root, left, right
        self.maxNum = -1000-1
        def resur(root):
            if root == None:
                return -1000-1
            leftVal = resur(root.left)
            rightVal = resur(root.right)
            self.maxNum = max(self.maxNum, root.val+leftVal+rightVal, leftVal, rightVal)
            return max(root.val, root.val+leftVal, root.val+rightVal)
        
        res = resur(root)
        return max(self.maxNum, res)
