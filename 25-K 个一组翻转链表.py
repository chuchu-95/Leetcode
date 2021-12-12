# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         node = ListNode(0)
#         node.next = head
#         current = node
#         copy = node.next
#         while copy:
#             cnt = 0
#             stack = []
#             while copy and cnt < k:
#                 stack.append(copy)
#                 copy = copy.next
#                 cnt += 1
#             if cnt != k:
#                 return node.next
#             while stack:
#                 current.next = stack.pop()
#                 current = current.next
#             current.next = copy
#         return node.next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node = ListNode(0)
        node.next = head
        pre = node
        while pre:
            pre = self.reversePart(pre, k)
        return node.next

    def reversePart(self, pre, k):
        # move to k+1 index as last point
        cnt = 0
        last = pre
        while cnt < k+1 and last != None:
            last = last.next
            cnt += 1
        if cnt != k+1 and last == None:
            return None
        # reverse
        end = pre.next
        cur = pre.next.next
        while cur != last:
            nt = cur.next
            cur.next = pre.next
            pre.next = cur
            end.next = nt
            cur = nt
        return end  