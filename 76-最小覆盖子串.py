class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # dict for t: count
        tDict = {}
        for tChar in t:
            if tChar in tDict:
                tDict[tChar] += 1
            else:
                tDict[tChar] = 1
        # find start char
        left = self.findStartChar(0, s, tDict)
        right = left
        cnt = 0
        res = ""
        sDict = {}
        for key in tDict.keys():
            sDict[key] = 0
        # traverse
        while right < len(s):
            if sDict[s[right]] < tDict[s[right]]:
                cnt += 1
            sDict[s[right]] += 1

            while left < len(s) and cnt == len(t):
                if res == "" or len(res) > len(s[left:right+1]):
                    res = s[left: right+1]
                # left
                if sDict[s[left]] == tDict[s[left]]:
                    cnt -= 1
                sDict[s[left]] -= 1
                left = self.findStartChar(left+1, s, tDict)

            right = self.findStartChar(right+1, s, tDict)
        return res
    def findStartChar(self, start, s, tDict):
        while start < len(s):
            if s[start] in tDict:
                return start
            else:
                start += 1
        return start