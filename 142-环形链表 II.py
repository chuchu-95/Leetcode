# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         pos = None
#         # get the length of circle
#         fast = head
#         slow = head
#         cirLen = 0
#         fLen = 0
#         sLen = 0
#         while fast and fast.next:
#             fast = fast.next.next
#             fLen += 2
#             slow = slow.next
#             sLen += 1
#             if fast == slow:
#                 cirLen = fLen - sLen
#                 break
#         if cirLen == 0:
#             return pos
#         # judge each node
#         while head:
#             curNode = head
#             cnt = 1
#             while cnt <= cirLen:
#                 curNode = curNode.next
#                 if curNode == head:
#                     pos = curNode
#                     return pos
#                 cnt += 1
#             head = head.next
#         return pos

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        pos = None
        # get the length of circle
        fast = head
        slow = head
        cirLen = 0
        fLen = 0
        sLen = 0
        while fast and fast.next:
            fast = fast.next.next
            fLen += 2
            slow = slow.next
            sLen += 1
            if fast == slow:
                cirLen = fLen - sLen
                break
        if cirLen == 0:
            return pos
        dect = head
        # detection
        while fast:
            if dect == fast:
                pos = dect
                return pos
            dect = dect.next
            fast = fast.next
        return pos
