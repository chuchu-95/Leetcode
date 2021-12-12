class Solution:
    def totalNQueens(self, n: int) -> int:
        column = set()
        diagonal_1 = set()
        diagonal_2 = set()
        cnt = self.helper(n, 0, column, diagonal_1, diagonal_2)
        return cnt
    def helper(self, n, row, column, diagonal_1, diagonal_2):
        if row == n:
            return 1
        else:
            count = 0
            for col in range(n):
                if col in column or row-col in diagonal_1 or row+col in diagonal_2:
                    continue
                column.add(col)
                diagonal_1.add(row-col)
                diagonal_2.add(row+col)
                count += self.helper(n, row+1, column, diagonal_1, diagonal_2)
                column.remove(col)
                diagonal_1.remove(row-col)
                diagonal_2.remove(row+col)
            return count