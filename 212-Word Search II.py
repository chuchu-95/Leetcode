# import collections
# class TrieNode:
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.isWord = False
    
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for w in word:
#             node = node.children[w]
#         node.isWord = True

#     def search(self, word):
#         node = self.root
#         for w in word:
#             node = node.children.get(w)
#             if not node:
#                 return False
#         return node.isWord

# class Solution:
#     def findWords(self, board, words):
#         res = []
#         trie = Trie()
#         node = trie.root
#         # add all word in words into Trie
#         for word in words:
#             trie.insert(word)
#         directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
#         m = len(board)
#         n = len(board[0])
#         for i in range(m):
#             for j in range(n):
#                 self.dfs(board, node, directions, i, j, "", res)
#         return res
#     def dfs(self, board, node, directions, i, j, cur, res):
#         if node.isWord:
#             res.append(cur)
#             node.isWord = False
#         if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
#             return 
#         tmp = board[i][j]
#         node = node.children.get(tmp)
#         if not node:
#             return 
#         board[i][j] = ""
#         for d in directions:
#             self.dfs(board, node, directions, i+d[0], j+d[1], cur+tmp, res)
#         board[i][j] = tmp


class TrieNode:
    def __init__(self):
        self.s = None
        self.nodeLst = [None] * 26

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def insert(s):
            node = root
            for sub in s:
                index = ord(sub) - ord('a')
                # judge if this node has been created
                if node.nodeLst[index] == None:
                    node.nodeLst[index] = TrieNode()
                node = node.nodeLst[index]
            node.s = s

        root = TrieNode()
        for word in words:
            insert(word)

        resSet = set()
        direction = [[-1,0], [1,0], [0,1],[0,-1]]
        m = len(board)
        n = len(board[0])
        visited = [[False for q in range(n)] for p in range(m)]
        for i in range(m):
            for j in range(n):
                cur = ord(board[i][j]) - ord('a')
                if root.nodeLst[cur] != None:
                    visited[i][j] = True
                    self.dfs(i, j, root.nodeLst[cur], resSet, direction, board, visited)
                    visited[i][j] = False
        return list(resSet)
                    
        
    def dfs(self, row, col, node, resSet, direction, board, visited):
        if node.s != None:
            resSet.add(node.s)
        
        for d in direction: 
            nxtRow = row+d[0]
            nxtCol = col+d[1]
            if nxtRow<0 or nxtCol<0 or nxtRow>=len(board) or nxtCol>=len(board[0]):
                continue
            if visited[nxtRow][nxtCol]:
                continue 
            curIndex = ord(board[nxtRow][nxtCol]) - ord('a')
            if node.nodeLst[curIndex] != None:
                visited[nxtRow][nxtCol] = True
                self.dfs(nxtRow, nxtCol, node.nodeLst[curIndex], resSet, direction, board, visited)
                visited[nxtRow][nxtCol] = False








    
