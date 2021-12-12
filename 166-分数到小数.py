class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        signal = ""
        if numerator*denominator < 0:
            signal = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        res = str(numerator // denominator)
        remainder = numerator % denominator
        if remainder == 0:
            return signal + res
        res += "."
        repeatMap = {}
        while remainder != 0:
            repeatMap[remainder] = len(res)
            remainder *= 10
            res += str(remainder // denominator)
            remainder %= denominator
            if remainder in repeatMap:
                idx = repeatMap[remainder]
                return signal + res[:idx] + "(" + res[idx:] + ")"
        return signal + res
