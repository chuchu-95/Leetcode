class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        tmp = self.helper(board, 0, 0)
    def helper(self, board, row, col):
        strList = ["1", "2", "3", "4", "5","6", "7", "8","9"]
        while row < 9 and col < 9:
            if board[row][col] == ".":
                break
            if col == 8:
                row += 1
                col = 0
            else:
                col += 1
        if row >= 9:
            return True
        #next row and column
        nextRow = row + col//8
        nextCol = (col+1) % 9
        for s in strList:
            if self.isValid(board, row, col, s):
                board[row][col] = s
                judgeNext = self.helper(board, nextRow, nextCol)
                if judgeNext:
                    return True
                board[row][col] = "."
        return False

    def isValid(self, board, row, col, s):
        #check row and column
        for i in range(9):
            if board[row][i] == s or board[i][col] == s:
                return False
        #check cube
        firstNumRow = 3*(row//3)
        firstNumCol = 3*(col//3)
        for m in range(3):
            for n in range(3):
                if board[firstNumRow+m][firstNumCol+n] == s:
                    return False
        return True