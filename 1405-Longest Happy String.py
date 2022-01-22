class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        numOccur = [['a', a], ['b', b], ['c', c]]
        res = ""
        while True:
            # ascend order
            numOccur.sort(key = lambda e : e[1])
            # judge
            if len(res) > 1 and res[-1] == res[-2] and numOccur[-1][0] == res[-1]:
                if numOccur[-2][1] > 0:
                    res += numOccur[-2][0]
                    numOccur[-2][1] -= 1
                else:
                    break
            else: 
                if numOccur[-1][1] > 0:
                    res += numOccur[-1][0]
                    numOccur[-1][1] -= 1
                else:
                    break
        return res
