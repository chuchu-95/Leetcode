class Solution:
    def countAndSay(self, n: int) -> str:
        ant = 1
        primStr = "1"
        while ant < n:
            count = 0
            currentStr = ""
            s = ""
            for i in range(len(primStr)):
                if primStr[i] == currentStr or currentStr == "":
                    count += 1
                else:
                    s += str(count) + currentStr
                    count = 1
                currentStr = primStr[i]
            s += str(count) + currentStr
            primStr = s
            ant += 1
        return primStr