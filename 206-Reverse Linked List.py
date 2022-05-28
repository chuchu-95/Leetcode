# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         preNode = None
#         nxtNode = None
#         curNode = head
#         while curNode:
#             nxtNode = curNode.next
#             curNode.next = preNode
#             preNode = curNode
#             curNode = nxtNode
#         return preNode
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = head
        print(pre.val)
        cur = pre.next
        print(cur.val)
        while cur:
            nxt = cur.next
            cur.next = pre
            print("nxt.val:")
            if nxt:
                print(nxt.val)
            print("cur.val:")
            print(cur.val)
            pre = cur
            cur = nxt
            print(pre.val)
            print(pre.next.val)
            if cur:
                print(cur.val)
                if cur.next:
                    print(cur.next.val)
        return pre
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
s = Solution()
s.reverseList(a)