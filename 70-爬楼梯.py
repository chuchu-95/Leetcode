# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1 or n == 2:
#             return n
#         # f(n) = f(n-1) + f(n-2)
#         fun = [None]*(n+1)
#         fun[1] = 1
#         fun[2] = 2
#         a = 3
#         while a <= n:
#             fun[a] = fun[a-1] + fun[a-2]
#             a += 1
#         return fun[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(3, n+1):
            cache = a
            a = b
            b = cache + b
        return b