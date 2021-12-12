# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        dummyA = headA
        dummyB = headB
        aLen = 0
        bLen = 0
        while dummyA:
            dummyA = dummyA.next
            aLen += 1
        while dummyB:
            dummyB = dummyB.next
            bLen += 1
        startA = aLen - min(aLen, bLen)
        startB = bLen - min(aLen, bLen)
        a = 0
        b = 0
        while a < startA:
            headA = headA.next
            a += 1
        while b < startB:
            headB = headB.next
            b += 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headB