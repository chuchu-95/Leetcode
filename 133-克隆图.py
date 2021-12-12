# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return node
        # old node to new node
        dic = {} 
        dic[node] = None
        queue = []
        queue.append(node)
        while queue:
            currOldNode = queue.pop(0)
            newNode = Node(currOldNode.val)
            dic[currOldNode] = newNode
            for nextOldNode in currOldNode.neighbors:
                # avoid circle
                if nextOldNode not in dic:
                    queue.append(nextOldNode)
        # connect as a graph
        for key in dic:
            dummy = dic[key]
            for value in key.neighbors:
                dummy.neighbors.append(dic[value])
        return dic[node]