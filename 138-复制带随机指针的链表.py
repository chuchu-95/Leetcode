# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        copyNode = {}
        p = head
        dummyNode = head
        while head:
            copyNode[head] = Node(head.val)
            head = head.next
        while dummyNode:
            if dummyNode.next == None:
                copyNode[dummyNode].next = None
            else:
                copyNode[dummyNode].next = copyNode[dummyNode.next]

            if dummyNode.random == None:
                copyNode[dummyNode].random = None
            else:
                copyNode[dummyNode].random = copyNode[dummyNode.random]
            dummyNode = dummyNode.next
        return copyNode[p]