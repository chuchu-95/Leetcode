class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp O(m*n) O(n)
        array = [[None for i in range(n)] for j in range(m)]
        # initialize
        array[0][0] = 0
        for p in range(n):
            array[0][p] = 1
        for q in range(m):
            array[q][0] = 1
        # dp function
        for a in range(1, m):
            for b in range(1, n):
                array[a][b] = array[a-1][b] + array[a][b-1]
        return array[m-1][n-1]