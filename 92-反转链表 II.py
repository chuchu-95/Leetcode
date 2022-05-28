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
# class Solution:
#     def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#         h = ListNode(0)
#         h.next = head
#         dummy = h
#         idx = 0
#         while idx < left:
#             if idx == left-1:
#                 preNode = h
#             h = h.next
#             idx += 1
#         mNode = h
#         while idx < right:
#             h = h.next
#             idx += 1
#         nNode = h
#         while mNode != nNode:
#             preNode.next = mNode.next
#             mNode.next = nNode.next
#             nNode.next = mNode
#             mNode = preNode.next
#         return dummy.next

# 2022/5/2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        pre = ListNode(0)
        pre.next = head
        dummy = pre
        idx = 1
        while head:
            if idx == left:
                end = head
                p = None
                while idx <= right:
                    nxt = head.next
                    head.next = p
                    p = head
                    head = nxt
                    idx += 1
                pre.next = p
                end.next = head
                break
            idx += 1
            head = head.next
            pre = pre.next
        return dummy.next
