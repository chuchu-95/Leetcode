# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        p = head
        while p:
            val = p.val
            while p.next and p.next.val == val:
                if p.next.next:
                    p.next = p.next.next
                else:
                    p.next = None
            p = p.next
        return head

