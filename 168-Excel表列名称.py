class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            res += chr(ord('A')+remainder)
            columnNumber //= 26
        return res[::-1]