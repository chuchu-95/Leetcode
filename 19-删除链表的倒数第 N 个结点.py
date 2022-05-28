# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         p = head
#         length = 0
#         while p != None:
#             p = p.next
#             length += 1
#         index = length - n

#         node = ListNode(0, head)
#         li = node
#         j = 0
#         while li.next != None and j < index:
#             li = li.next
#             j += 1
#         li.next = li.next.next
#         return node.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        while n >= 0 and fast:
            fast = fast.next
            n -= 1
        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next
        if slow.next:
            slow.next = slow.next.next
        return dummy.next