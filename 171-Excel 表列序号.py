class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        system = 1
        for idx in range(len(columnTitle)-1, -1, -1):
            cur = ord(columnTitle[idx])-ord('A')+1
            res += (cur*system)
            system *= 26
        return res
