class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]
        # set walls and guards
        for w in walls:
            grid[w[0]][w[1]] = 1
        for g in guards:
            grid[g[0]][g[1]] = 1
        # dfs according to guards
        direct = [[-1,0], [1,0], [0,1], [0,-1]]
        for x, y in guards:
            for d in direct:
                i, j = x, y
                while i+d[0] >= 0 and i+d[0] < m and j+d[1] >= 0 and j+d[1] < n and grid[i+d[0]][j+d[1]] != 1:
                    i += d[0]
                    j += d[1]
                    grid[i][j] = 2
        cnt = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    cnt += 1      
        return cnt