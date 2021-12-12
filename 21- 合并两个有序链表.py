# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        li = ListNode(0)
        tp = li
        while l1 and l2:
            num1 = l1.val
            num2 = l2.val
            if num1 <= num2:
                tp.next = ListNode(num1)
                l1 = l1.next
            else:
                tp.next = ListNode(num2)
                l2 = l2.next
            tp = tp.next
        if l1:
            tp.next = l1
        if l2:
            tp.next = l2

        return li.next