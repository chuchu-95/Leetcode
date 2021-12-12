class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        step = [[None for i in range(len(grid[0]))] for j in range(len(grid))]
        # initalize
        step[0][0] = grid[0][0]
        for col in range(1, len(grid[0])):
            step[0][col] = grid[0][col] + step[0][col-1]
        for row in range(1, len(grid)):
            step[row][0] = grid[row][0] + step[row-1][0]
        # start
        for m in range(1, len(grid)):
            for n in range(1, len(grid[0])):
                step[m][n] = min(step[m-1][n]+grid[m][n], step[m][n-1]+grid[m][n])
        return step[len(grid)-1][len(grid[0])-1]