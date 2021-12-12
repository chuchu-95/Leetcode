class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = "0"
        pA = len(a) - 1
        pB = len(b) - 1
        while pA >= 0 or pB >= 0:
            if pA < 0:
                subA = "0"
            else:
                subA = a[pA]
            if pB < 0:
                subB = "0"
            else:
                subB = b[pB]
            rTuple = self.BinarySum(subA, subB)
            t2 = self.BinarySum(rTuple[0], carry)
            sum = t2[0]
            carry = rTuple[1]
            if t2[1] == "1":
                carry = t2[1]
            res += sum
            pA -= 1
            pB -= 1
        if carry == "1":
            res += carry
        return res[::-1]

    def BinarySum(self, st1, st2):
        if st1 == "1" and st2 == "1":
            return "0", "1"
        elif st1 == "0" and st2 == "0":
            return "0", "0"
        else:
            return "1", "0"