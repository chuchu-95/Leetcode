# QuickSort
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head == None or head.next == None:
#             return head
#         else:
#             less = ListNode(0)
#             pLess = less
#             greater = ListNode(0)
#             pGreat = greater
#             pivot = head.val
#             cur = head.next
#             while cur:
#                 value = cur.val    
#                 if value < pivot:
#                     less.next = cur
#                     less = less.next
#                 else:
#                     greater.next = cur
#                     greater = greater.next
#                 cur = cur.next
#             greater.next = None
#             less.next = head
#             head.next = None

#             lss = self.sortList(pLess.next)
#             gre = self.sortList(pGreat.next)

#             head.next = gre
#             return lss


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        # dfs
        # first cut until signal head or None
        if head == None or head.next == None:
            return head
        # 1.cut from middle, use fast and slow approach
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        headAnother = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(headAnother)
        # 2.merge two sorted list, like Leetcode21
        temp = ListNode(0)
        dummy = temp
        while left and right:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        if left:
            temp.next = left
        if right:
            temp.next = right
        return dummy.next