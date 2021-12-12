class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        li = []
        num1 = num1[::-1]
        num2 = num2[::-1]
        point1 = 0
        point2 = 0
        carry = 0
        part = ""
        while point2 < len(num2):
            muti1 = int(num1[point1])
            muti2 = int(num2[point2])
            sum = (muti1*muti2 + carry) % 10
            carry = (muti1*muti2 + carry) // 10
            part += str(sum)
            point1 += 1
            if point1 == len(num1):
                if carry > 0:
                    part += str(carry)
                carry = 0
                point1 = 0
                li.append(part)
                point2 += 1
                part = ""

        result = 0
        supple = 0
        for n in li:
            nInt = int(n[::-1])
            if supple > 0:
                nInt = nInt * pow(10, supple)
            result += nInt
            supple += 1
        return str(result)      
