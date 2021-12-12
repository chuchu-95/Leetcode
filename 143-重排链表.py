# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if head == None:
#             return head
#         preNode = ListNode(0)      
#         midNode = head  #slow
#         point = head  #fast
#         preNode.next = midNode
#         while point and point.next:
#             preNode = preNode.next
#             midNode = midNode.next
#             point = point.next.next
#         if point == None:
#             midNode = preNode
        
#         while head != midNode:
#             nextNode = head.next
#             endNode = midNode 
#             while endNode.next:
#                 store = endNode.next
#                 if endNode.next.next == None:
#                     endNode.next = None
#                 endNode = store
#             endNode.next = head.next
#             head.next = endNode

#             head = nextNode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return head
        midNode = self.findMid(head)
        reverseNode = self.reverse(midNode)
        midNode.next = None
        orignNode = head
        # merge
        self.merge(orignNode, reverseNode)

    def findMid(self, head):
        preNode = ListNode(0)      
        midNode = head  #slow
        point = head  #fast
        preNode.next = midNode
        while point and point.next:
            preNode = preNode.next
            midNode = midNode.next
            point = point.next.next
        if point == None:
            midNode = preNode
        return midNode

    def reverse(self, head):
        p = head.next
        head.next = None
        while p:
            q = p.next
            p.next = head.next
            head.next = p
            p = q
        return head.next
    
    def merge(self, oNode, rNode):
        while oNode and rNode:
            oCache = oNode.next
            rCache = rNode.next
            rNode.next = oNode.next
            oNode.next = rNode
            oNode = oCache
            rNode = rCache





    
        
