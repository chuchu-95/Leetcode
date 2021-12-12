class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, res, [], 0, len(s))
        return res
    def dfs(self, s, res, lst, start, sLen):
        if start == sLen:
            res.append(lst[:])
        else:
            for idxEnd in range(start, sLen):
                if not self.isPalindrome(s, start, idxEnd):
                    continue
                lst.append(s[start: idxEnd+1])
                self.dfs(s, res, lst, idxEnd+1, sLen)
                lst.pop()
                
    def isPalindrome(self, s, p1, p2):
        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True