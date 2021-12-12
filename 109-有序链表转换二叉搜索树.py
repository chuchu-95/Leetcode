# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        #set head
        h = ListNode(0)
        h.next = head
        dummy = h
        mid, mL = self.getMiddleNum(h)
        for i in range(mL-1):
            h = h.next
        h.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(dummy.next)
        root.right = self.sortedListToBST(mid.next)
        return root

        
    def getMiddleNum(self, head):
        midLen = 0
        p = head    #fast
        q = head    #slow
        while p:
            p = p.next
            if p:
                p = p.next
            q = q.next
            midLen += 1
        return q, midLen
        

