# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         # row
#         i = 0
#         while i < 9:
#             dic = {}
#             for j in range(9):
#                 st = board[i][j]
#                 if st != ".":
#                     if st in dic:
#                         return False
#                     else:
#                         dic[st] = 1
#             i += 1
#         # column
#         h = 0
#         while h < 9:
#             dic = {}
#             for k in range(9):
#                 st = board[k][h]
#                 if st != ".":
#                     if st in dic:
#                         return False
#                     else:
#                         dic[st] = 1
#             h += 1
        
#         # table
#         n = 0
#         while n < 9:
#             dic = {}
#             for a in range(3):
#                 for b in range(3):
#                     st = board[a+(n//3)*3][b+(n%3)*3]
#                     if st != ".":
#                         if st in dic:
#                             return False
#                         else:
#                             dic[st] = 1
#             n += 1
#         return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set([])
            col_set = set([])
            cube_set = set([])
            for j in range(9):
                #row
                primLenRow = len(row_set)
                row_set.add(board[i][j])
                if board[i][j] != "." and primLenRow == len(row_set):
                    return False
                #column
                primLenCol = len(col_set)
                col_set.add(board[j][i])
                if board[j][i] != "." and primLenCol == len(col_set):
                    return False
                #cube
                primLenCube = len(cube_set)
                firstNumRow = 3*(i//3)
                firstNumCol = 3*(i%3)
                word = board[firstNumRow+ j//3][firstNumCol+ j%3]
                cube_set.add(word)
                if word != "." and primLenCube == len(cube_set):
                    return False
        return True