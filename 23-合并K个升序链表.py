# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    from heapq import heapify, heappush, heappop    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        priQueue = []
        heapify(priQueue)
        head = ListNode(0)
        copy = head
        i = 0
        for lst in lists:
            if lst:
                heappush(priQueue, (lst.val, i))
            i += 1
        while priQueue:
            num,index = heappop(priQueue)
            node = lists[index]
            copy.next = node
            copy = copy.next
            if node.next:
                heappush(priQueue, (node.next.val, index))
            lists[index] = node.next
        return head.next