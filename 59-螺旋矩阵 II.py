class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for _ in range(n)] for _ in range(n)]
        i = 0   # row
        j = 0   # column
        direct = 1
        cir = 0
        add_i = 0
        add_j = 1
        turn = n
        cnt = 0
        for num in range(1, n*n+1):
            if cnt == turn-1:
                cnt = 0
                cir += 1
                if cir == 0:
                    direct *= -1
                    cnt = -1
                if cir == 2:
                    direct *= -1
                if cir == 3:
                    turn -= 2
                    cir = -1
                    cnt = -1
                add_i, add_j = add_j, add_i
            matrix[i][j] = num
            i += add_i * direct
            j += add_j * direct
            cnt += 1
        return matrix
