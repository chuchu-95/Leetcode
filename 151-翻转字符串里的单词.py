class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        sLen = len(s)
        start = sLen - 1
        end = sLen - 1
        while start > -1 and end > -1:
            if s[end].isalnum():
                start = end
                while s[start-1] != " " and start != 0:
                    start -= 1
                res += (s[start: end+1] + " ")
                end = start - 1
            else:
                end -= 1
        return res[:-1]