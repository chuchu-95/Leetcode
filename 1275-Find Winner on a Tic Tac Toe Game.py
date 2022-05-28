class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [[0 for r in range(3)] for player in range(2)]
        cols = [[0 for c in range(3)] for player in range(2)]
        diagonal = [[0 for d in range(2)] for player in range(2)]
        players = {0: 'A', 1: 'B'}

        for i in range(len(moves)):
            move = moves[i]
            #'A'
            player = i % 2
            rows[player][move[0]] += 1
            if rows[player][move[0]] == 3:
                return players[player]
            cols[player][move[1]] += 1
            if cols[player][move[1]] == 3:
                return players[player]
            if move[0] == move[1]:
                diagonal[player][0] += 1
                if diagonal[player][0] == 3:
                    return players[player]
            if move[0] + move[1] == 2:
                diagonal[player][1] += 1
                if diagonal[player][1] == 3:
                    return players[player]
        return "Draw" if len(moves) == 9 else "Pending"
