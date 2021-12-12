class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #initialize first row and column
        firstRowJudge = False
        firstColJudge = False
        #row
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                firstRowJudge = True
                break
        #col
        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                firstColJudge = True
                break
        #start
        for m in range(1, len(matrix)):
            for n in range(1, len(matrix[0])):
                if matrix[m][n] == 0:
                    matrix[m][0] = 0
                    matrix[0][n] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if firstRowJudge:
            for ro in range(len(matrix)):
                matrix[ro][0] = 0
        if firstColJudge:
            for co in range(len(matrix[0])):
                matrix[0][co] = 0 
        