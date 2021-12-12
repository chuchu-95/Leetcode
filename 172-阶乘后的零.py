# class Solution:
#     def trailingZeroes(self, n: int) -> int:  
#         if n == 0:
#             return 0
#         res = self.trailing(n)
#         str_res = str(res)
#         resLen = len(str_res)
#         cnt = 0
#         for i in range(resLen-1, -1, -1):
#             if str_res[i] == '0':
#                 cnt += 1
#             else:
#                 break
#         return cnt

#     def trailing(self, num):
#         if num == 1:
#             return num
#         else:
#             return num * self.trailing(num-1)

class Solution:
    def trailingZeroes(self, n: int) -> int:  
        cnt = 0
        while n > 0:
            cnt += (n // 5)
            n //= 5
        return cnt