# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        p = ListNode(0)
        realNode = p
        preNode = p
        curNode = head
        while curNode:
            if (preNode == p or preNode.val != curNode.val) and (curNode.next == None or curNode.next.val != curNode.val):
                realNode.next = curNode
                realNode = curNode
            preNode = curNode
            curNode = curNode.next
            preNode.next = None
        return p.next
            
