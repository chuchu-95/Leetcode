class Solution:
    def findRepeatedDnaSequences(self, s: str):
        res = []
        if len(s) < 10:
            return res
        subSet = set()
        for i in range(len(s)-9):
            subStr = s[i: i+10]
            if subStr in subSet:
                res.append(subStr)
            else:
                subSet.add(subStr)
        return list(set(res))