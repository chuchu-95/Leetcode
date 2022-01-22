class Solution:
    def numIslands(self, grid) -> int: 
        # row, col                
        self.move = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        islandSum = 0
        for curRow in range(len(grid)):
            for curCol in range(len(grid[0])):
                if grid[curRow][curCol] == '1':
                    self.dfs(grid, curRow, curCol)
                    # if has 1, there must have a island
                    islandSum += 1
        return islandSum
    
    def dfs(self, grid, row, col):
        if row < len(grid) and col < len(grid[0]) and row >= 0 and col >= 0 and grid[row][col] == '1':
            for direct in self.move:
                grid[row][col] = '0'
                self.dfs(grid, row+direct[0], col+direct[1])
        else:
            return