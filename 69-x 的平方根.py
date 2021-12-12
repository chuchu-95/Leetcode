# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0 or x == 1:
#             return x
#         # Binary search O(logn)
#         low = 0
#         high = x
#         while low <= high:
#             mid = low + (high - low)//2
#             if mid * mid > x:
#                 high = mid - 1
#             elif mid * mid <= x:
#                 res = mid
#                 low = mid + 1
#         return res

class Solution:
    def mySqrt(self, x: int) -> int:
        # Using function: x^2 - c = 0
        if x == 0:
            return x
        x0 = x
        while True:
            xi = 0.5 * (x0 + x/x0)
            if abs(x0-xi) < 1e-6:
                return int(xi)
            x0 = xi
        

        
