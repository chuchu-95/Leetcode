# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        length = 0
        while p != None:
            p = p.next
            length += 1
        index = length - n

        node = ListNode(0, head)
        li = node
        j = 0
        while li.next != None and j < index:
            li = li.next
            j += 1
        li.next = li.next.next
        return node.next