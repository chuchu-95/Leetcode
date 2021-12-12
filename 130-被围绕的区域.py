class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowLen = len(board)-1
        colLen = len(board[0])-1
        direct = [[-1,0],[1,0],[0,1],[0,-1]]
        #dfs
        def dfs(x, y):
            board[x][y] = "Z"
            for d in direct:
                t_x = x + d[0]
                t_y = y + d[1]
                if t_x > 0 and t_x <= rowLen and t_y > 0 and t_y <= colLen and board[t_x][t_y] == "O":
                    dfs(t_x, t_y)

        #if char in board's boarder, sign it as "Z"
        for row in range(len(board)):
            if board[row][0] == "O":
                board[row][0] = "Z"
            if board[row][colLen] == "O":
                board[row][colLen] = "Z"
        for col in range(len(board[0])):
            if board[0][col] == "O":
                board[0][col] = "Z"
            if board[rowLen][col] == "O":
                board[rowLen][col] = "Z"
        
        for r in range(len(board)):
            if board[r][0] == "Z":
                dfs(r, 0)
            if board[r][colLen] == "Z":
                dfs(r, colLen)
        for c in range(len(board[0])):
            if board[0][c] == "Z":
                dfs(0, c)
            if board[rowLen][c] == "Z":
                dfs(rowLen,c)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Z":
                    board[i][j] = "O"