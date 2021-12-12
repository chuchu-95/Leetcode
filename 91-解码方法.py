class Solution:
    def numDecodings(self, s: str) -> int:
        state = [0] * (len(s)+1)
        state[0] = 1
        state[1] = 1
        if s[0] == '0':
            return 0
        for i in range(1, len(s)):
            if s[i] == '0':
                if int(s[i-1]) >= 1 and int(s[i-1]) <= 2:
                    state[i+1] = state[i-1]
                else:
                    return 0
            else:
                if s[i-1] == '0' or int(s[i-1:i+1]) > 26:
                    state[i+1] = state[i]
                else:
                    state[i+1] = state[i] + state[i-1]

        return state[len(s)]
