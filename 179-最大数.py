class Solution:
    def largestNumber(self, nums) -> str:
        # part of it is the biggest
        import functools
        # sequence=> y before x
        compare = lambda x, y : 1 if x+y < y+x else -1
        strNums = list(map(str, nums))
        strNums.sort(key = functools.cmp_to_key(compare))
        res = ""
        for s in strNums:
            res += s
        start = 0
        for sub in res:
            if sub == '0' and start != len(res)-1:
                start += 1
            else:
                break
        return res[start:]