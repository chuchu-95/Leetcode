# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#         h = ListNode(0)
#         h.next = head
#         dummy = h
#         part = []
#         idx = 0
#         while idx <= right:
#             if idx == left-1:
#                 p = h
#             if idx >= left:
#                 part.append(h.val)
#             h = h.next
#             idx += 1
#         while part != []:
#             p.next = ListNode(part.pop())
#             p = p.next
#         p.next = h
#         return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        h = ListNode(0)
        h.next = head
        dummy = h
        idx = 0
        while idx < left:
            if idx == left-1:
                preNode = h
            h = h.next
            idx += 1
        mNode = h
        while idx < right:
            h = h.next
            idx += 1
        nNode = h
        while mNode != nNode:
            preNode.next = mNode.next
            mNode.next = nNode.next
            nNode.next = mNode
            mNode = preNode.next
        return dummy.next
