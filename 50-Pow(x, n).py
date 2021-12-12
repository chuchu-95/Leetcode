class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or n == 0:
            return 1
        elif n < 0:
            return 1 / (x * self.myPow(x, -n-1))
        else:
            res = 1
            while n != 1:
                if n % 2 == 1:
                    res *= x
                n //= 2
                x *= x
        return res * x