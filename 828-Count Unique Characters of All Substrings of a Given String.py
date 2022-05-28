class Solution:
    def uniqueLetterString(self, s: str) -> int:
        result = 0
        # initialize
        index = [[-1, -1]] * 26
        for i, c in enumerate(s):
            posit = ord(c) - 65
            lastPre, pre = index[posit]
            result += (i-pre) * (pre-lastPre)
            index[posit] = [pre, i]
        for rest in index:
            result += (rest[1]-rest[0]) * (len(s)-rest[1])
        return result
