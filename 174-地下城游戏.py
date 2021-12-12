# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         #dfs
#         rowLength = len(dungeon)
#         colLength = len(dungeon[0])
#         cache = [[True for i in range(colLength)]for j in range(rowLength)]

#         return self.dfs(rowLength, colLength, dungeon, 0, 0, cache)+1

#     def dfs(self, rowLen, colLen, dungeon, row, col, cache):
#         # boundry condition
#         if row > rowLen-1 or col > colLen-1:
#             return float('inf')

#         if cache[row][col] != True:
#             return cache[row][col]
        
#         # exit condition
#         if row == rowLen-1 and col == colLen-1:
#             # the end position need no blood
#             if dungeon[row][col] > 0:
#                 cache[row][col] = 0
#                 return 0
#             else:
#                 cache[row][col] = -dungeon[row][col]
#                 return -dungeon[row][col]
#         # other
#         leftMin = self.dfs(rowLen, colLen, dungeon, row, col+1, cache)
#         downMin = self.dfs(rowLen, colLen, dungeon, row+1, col, cache)

#         # dungeon[row][col] might be positive num
#         curMin = min(leftMin, downMin) - dungeon[row][col]
#         # cur position must can goto next
#         if curMin < 0:
#             cache[row][col] = 0
#             return 0
#         cache[row][col] = curMin
#         return curMin


class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        # dp
        rowLen = len(dungeon)
        colLen = len(dungeon[0])
        dp =[[0 for i in range(colLen)]for j in range(rowLen)]
        # initialize
        dp[rowLen-1][colLen-1] = max(0, -dungeon[rowLen-1][colLen-1])
        #bigger than zero means this cell needs init blood
        for col in range(colLen-2, -1, -1):
            dp[rowLen-1][col] = max(0, dp[rowLen-1][col+1]-dungeon[rowLen-1][col])
        for row in range(rowLen-2, -1, -1):
            dp[row][colLen-1] = max(0, dp[row+1][colLen-1]-dungeon[row][colLen-1])
        # start
        for i in range(rowLen-2, -1, -1):
            for j in range(colLen-2, -1, -1):
                # min(dp[i+1][j], dp[i][j+1]) must bigger than 0 or equal to 0
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                # dp[i][j] might less than 0 because abs(dungeon[i][j]) is bigger
                dp[i][j] = max(dp[i][j], 0)
        return dp[0][0] + 1
