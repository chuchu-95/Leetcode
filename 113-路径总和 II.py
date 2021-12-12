# # Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def pathSum(root, targetSum) :
#     result = []
#     sub = list()
#     def helper(root, targetSum):
#         if not root:
#             return 
#         sub.append(root.val)
#         targetSum -= root.val
#         if root.left == None and root.right == None and targetSum == 0:
#             result.append(sub)
#         helper(root.left, targetSum)
#         helper(root.right, targetSum)
#         sub.pop()
        
#     helper(root, targetSum)
#     return result

# T = TreeNode(5)
# a = TreeNode(4)
# b = TreeNode(8)
# T.left = a
# T.right = b
# c = TreeNode(11)
# d = TreeNode(7)
# e = TreeNode(2)
# f = TreeNode(13)
# h = TreeNode(4)
# i = TreeNode(5)
# j = TreeNode(1)
# a.left = c
# c.left = d
# c.right = e
# b.left = f
# b.right = h
# h.left = i
# h.right = j


# print(pathSum(T,22))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        sub = []
        def helper(root, targetSum):
            if not root:
                return 
            sub.append(root.val)
            if root.left == None and root.right == None and targetSum == root.val:
                result.append(list(sub))
            helper(root.left, targetSum-root.val)
            helper(root.right, targetSum-root.val)
            sub.pop()
        helper(root, targetSum)
        return result
        