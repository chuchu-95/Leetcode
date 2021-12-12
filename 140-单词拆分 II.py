class Solution:
    def wordBreak(self, s: str, wordDict):
        res = []
        res = self.helper(0, s, wordDict, "", res)
        return res
    def helper(self, start, s, wordDict, sub, res):
        if start == len(s):
            res.append(sub[:-1])
        else:
            i = start
            for j in range(start+1, len(s)+1):
                if s[i: j] in wordDict:
                    self.helper(j, s, wordDict, sub+(s[i: j] + " "), res) 
        return res

