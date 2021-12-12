class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        node_head = ListNode(0)
        cur = node_head  
        while l1 or l2:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            cur.next = ListNode((val1 + val2 + carry) % 10)
            carry = (val1 + val2 + carry) // 10
            #l1,l2,cur pointers to the next position
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
            cur = cur.next 
        if carry > 0:
            cur.next = ListNode(carry)
        return node_head.next

def printLink(li):
    li_head = li
    while li_head:
        print(li_head.next)
        li_head = li_head.next
