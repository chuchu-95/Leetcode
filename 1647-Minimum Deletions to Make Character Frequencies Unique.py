class Solution:
    def minDeletions(self, s: str) -> int:
        import collections
        res, dicFreq, cntSet = 0, collections.Counter(s), set()
        for sub, freq in dicFreq.items():
            if freq in cntSet:
                while freq > 0 and freq in cntSet:
                    freq -= 1
                    res += 1
            cntSet.add(freq)
        return res