class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose row to column
        i = 0
        j = 0
        while i != len(matrix):
            if j == len(matrix):
                i += 1
                j = i
            else:
                change = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = change
                j += 1
        # mirror symmetry
        m = 0
        left = 0
        right = len(matrix)-1
        while m != len(matrix):
            if left == right or left -right == 1:
                left = 0
                right = len(matrix)-1
                m += 1
            else:
                help = matrix[m][left]
                matrix[m][left] = matrix[m][right]
                matrix[m][right] = help
                left += 1
                right -= 1