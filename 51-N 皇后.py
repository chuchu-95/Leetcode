class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        queen = [None]*n
        column = set()
        diagonal_1 = set()
        diagonal_2 = set()
        res = []
        self.helper(queen, n, 0, res, column, diagonal_1, diagonal_2)
        return res

    def helper(self, queen, n, row, res, column, diagonal_1, diagonal_2):
        if row == n:
            board = self.generate(queen, n)
            res.append(board)
        else:
            for col in range(n):
                if col in column or row-col in diagonal_1 or row+col in diagonal_2:
                    continue
                queen[row] = col
                column.add(col)
                diagonal_1.add(row-col)
                diagonal_2.add(row+col)
                self.helper(queen, n, row+1, res, column, diagonal_1, diagonal_2) 
                column.remove(col)
                diagonal_1.remove(row-col)
                diagonal_2.remove(row+col)
    def generate(self, queen, n):
        board = []
        for i in range(n):
            q = ["." for i in range(n)]
            q[queen[i]] = "Q"
            part = "".join(q)
            board.append(part)
        return board