# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(min, max):
            result = [] 
            if min > max:
                return result
            for rt in range(min, max+1):
                leftList = helper(min, rt-1)
                rightList = helper(rt+1, max)
                if leftList == [] and rightList == []:
                    root = TreeNode(rt)
                    result.append(root)
                elif leftList == [] and rightList != []:
                    for rlst in rightList:
                        root = TreeNode(rt)
                        root.right = rlst
                        result.append(root)
                elif leftList != [] and rightList == []:
                    for llst in leftList:
                        root = TreeNode(rt)
                        root.left = llst
                        result.append(root)
                else:
                    for l in leftList:
                        for r in rightList:
                            root = TreeNode(rt)
                            root.left = l
                            root.right = r
                            result.append(root)
            return result
        return helper(1, n)
        