# class Solution:
#     def strWithout3a3b(self, a: int, b: int) -> str:
#         curNum = [['a', a], ['b', b]]
#         res = ""
#         while True:
#             # asend sequence
#             curNum.sort(key = lambda arr: arr[-1])
#             if len(res) > 1 and res[-1] == res[-2] and res[-1] != curNum[-2][0]:
#                 if curNum[-2][1] > 0:
#                     res += curNum[-2][0]
#                     curNum[-2][1] -= 1
#                 else:
#                     break
#             else:
#                 if curNum[-1][1] > 0:
#                     res += curNum[-1][0]
#                     curNum[-1][1] -= 1
#                 else:
#                     break
#         return res
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ""
        # max, min   
        # i  >  j
        i, j = a, b
        a, b = 'a', 'b'
        if j > i:
            i, j = j, i
            a, b = b, a
        while i > 0:
            # i is always bigger than j
            i -= 1
            res += a
            if i > j:
                i -= 1
                res += a
            if j > 0:
                j -= 1
                res += b
        return res