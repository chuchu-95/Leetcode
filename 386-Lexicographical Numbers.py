# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         #dfs
#         res = []
#         def dfs(num):
#             if num > n:
#                 return 
#             res.append(num)
#             for i in range(num*10, num*10 + 10):
#                 dfs(i)
#         for num in range(1, 10):
#             dfs(num)
#         return res
        

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        num = 1
        while len(res) < n:
            while num <= n:
                res.append(num)
                num *= 10
            while num % 10 == 9 or num > n:
                num //= 10
            num += 1
        return res