# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None:
            return head
        p = None
        dummy = ListNode(0)
        dummy.next = head
        dHead = dummy
        while dummy.next:
            if dummy.next.val >= x:
                p = dummy.next
                dummy.next = None
                break
            dummy = dummy.next
        if p == None:
            return dHead.next
        pHead = p
        while p.next:
            if p.next.val < x:
                dummy.next = p.next
                dummy = dummy.next
                # dummy.next = None
                if p.next.next == None:
                    p.next = None
                else:
                    p.next = p.next.next
            else:
                p = p.next
        dummy.next = pHead
        return dHead.next
