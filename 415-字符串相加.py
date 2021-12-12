class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        maxLen = max(len(num1), len(num2))
        point1 = 0
        point2 = 0
        carry = 0
        result = ""
         
        while point1 < len(num1) or point2 < len(num2):
            if point1 < len(num1):
                addend1 = int(num1[point1])
            else:
                addend1 = 0
            if point2 < len(num2):
                addend2 = int(num2[point2])
            else:
                addend2 = 0
            sum = (addend1 + addend2 + carry) % 10
            result += str(sum)
            carry = (addend1 + addend2 + carry) // 10
            if point1 < len(num1):
                point1 += 1
            if point2 < len(num2):
                point2 += 1
        if carry > 0:
            result += str(carry)
        return result[::-1]
            