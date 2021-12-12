# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        start = ListNode(0)
        start.next = head
        end = head
        cur = head.next
        while cur:
            if cur.val >= end.val:
                end = end.next
            else:
                dummy = start
                while cur.val > dummy.next.val:
                    dummy = dummy.next
                end.next = cur.next
                cur.next = dummy.next
                dummy.next = cur
            cur = end.next
        return start.next