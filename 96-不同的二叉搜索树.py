class Solution:
    def numTrees(self, n: int) -> int:
        # initialize
        state = [0] * (n+1)
        state[0] = 1
        state[1] = 1
        for i in range(2, n+1):
            for j in range(0, i):
                state[i] += (state[j] * state[i-j-1])
        return state[n]
        