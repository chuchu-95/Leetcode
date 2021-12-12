class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend * divisor < 0:
            sign = -1
        res = 0
        result = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        divisor_move = divisor
        while dividend >= divisor:
            if divisor_move <= dividend:
                divisor_move = divisor_move << 1
                result = result << 1
            elif divisor_move > dividend:
                divisor_move = divisor_move >> 1
                dividend = dividend - divisor_move
                divisor_move = divisor
                result = result >> 1
                res += result
                result = 1  
        a = (1<<31) - 1
        if res*sign > a:
            return a 
        return res*sign