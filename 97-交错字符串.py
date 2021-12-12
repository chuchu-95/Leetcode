class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        state = [[False for i in range(len(s1)+1)] for j in range(len(s2)+1)]
        state[0][0] = True
        for idx in range(len(s3)):
            s1Len = 0
            # for s1Len in range(min(idx+2, len(s1)+1)):
            while s1Len <= idx+1 and s1Len <= len(s1):
                s2Len = idx + 1 - s1Len
                if s2Len > len(s2):
                    s1Len += 1
                    continue
                if (s2Len>0 and state[s2Len-1][s1Len] and s3[idx]==s2[s2Len-1]) or (s1Len>0 and state[s2Len][s1Len-1] and s3[idx]==s1[s1Len-1]):
                    state[s2Len][s1Len] = True
                s1Len += 1

        return state[len(s2)][len(s1)]