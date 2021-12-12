# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        newHead = ListNode(0)
        length = 0
        p = head
        while p != None:
            length += 1
            if p.next == None:
                p.next = head
                break
            p = p.next
        cnt = k % length
        index = length - cnt
        n = 0
        while n < index:
            p = p.next
            n += 1
        newHead.next = p.next
        p.next = None
        return newHead.next
            