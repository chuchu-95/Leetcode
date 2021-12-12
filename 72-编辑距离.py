class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp
        dp = [[None for w2 in range(len(word2)+1)] for w1 in range(len(word1)+1)]
        #initalize
        dp[0][0] = 0
        for m in range(1, len(word1)+1):
            dp[m][0] = m
        for n in range(1, len(word2)+1):
            dp[0][n] = n
        #start
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[len(word1)][len(word2)]