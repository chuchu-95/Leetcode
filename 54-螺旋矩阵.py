class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        i = 0
        j = 0
        direct = 1
        add_row = 0
        add_col = 1
        turn_row = len(matrix[0]) 
        turn_col = len(matrix) 
        point = 0   # make a turn
        time = 0
        for cnt in range(len(matrix[0])*len(matrix)):
            if point == turn_row-1:
                time += 1
                add_row, add_col = add_col, add_row
                turn_row, turn_col = turn_col, turn_row
                point = 0
                if time == 3:
                    turn_row -= 2
                    turn_col -= 2
                    time = -1
                    point = -1
                elif time == 2:
                    direct *= -1
                elif time == 0:
                    point = -1
                    direct *= -1
            result.append(matrix[i][j])
            # next
            i += (add_row * direct)
            j += (add_col * direct)
            point += 1
        return result