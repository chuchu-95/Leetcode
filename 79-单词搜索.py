class Solution: 
    def exist(self, board, word: str) -> bool:
        dir_row = [-1, 0, 1, 0]
        dir_col = [0, -1, 0, 1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, 0, dir_row, dir_col, board, word):
                    return True
        return False


    def dfs(self, i, j, idx, dir_row, dir_col, board, word):
        if idx == len(word)-1:
            return board[i][j] == word[idx]

        if board[i][j] == word[idx]:
            cache = board[i][j]
            board[i][j] = ""
            for d in range(4):
                row = i + dir_row[d]
                col = j + dir_col[d]
                # out of index or has been checked
                if self.inBoard(row, col, board) and board[row][col] != "" :
                    if self.dfs(row, col, idx+1, dir_row, dir_col, board, word):
                        return True
            board[i][j] = cache
        return False

    def inBoard(self, row, col, board):
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])
      