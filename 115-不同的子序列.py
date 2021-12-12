class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #state[i][j]  i: t; j : s
        state = [[0 for b in range(len(s)+1)] for a in range(len(t)+1)]
        # initialize
        for fst in range(len(s)+1):
            state[0][fst] = 1
        # start
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if s[j-1] == t[i-1]:
                    state[i][j] = state[i-1][j-1] + state[i][j-1]
                else:
                    state[i][j] = state[i][j-1]
        return state[len(t)][len(s)]


