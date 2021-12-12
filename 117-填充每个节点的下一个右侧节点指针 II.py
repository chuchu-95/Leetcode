"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        node = root
        while node:
            curr = node
            pre = Node(0)
            dummy = pre
            while curr:
                if curr.left:
                    pre.next = curr.left
                    pre = pre.next
                if curr.right:
                    pre.next = curr.right
                    pre = pre.next
                curr = curr.next
            node = dummy.next
        return root
        