# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = ListNode(0)
        p.next = head
        dummy = p
        while dummy.next and dummy.next.next:
            node1 = dummy.next
            node2 = dummy.next.next
            dummy.next = node2
            node1.next = node2.next
            dummy.next.next = node1
            dummy = dummy.next.next
        return p.next