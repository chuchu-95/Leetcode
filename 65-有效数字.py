class Solution:
    def isNumber(self, s: str) -> bool:
        idx = 0
        judgeDigit = False
        # judge space
        while idx < len(s) and s[idx] == " ":
            idx += 1
        # judge sign
        if s[idx] == "+" or s[idx] == "-":
            idx += 1
        # judge digit before point
        while idx < len(s) and s[idx].isdigit():
            judgeDigit = True
            idx += 1
        # judge point
        if idx < len(s) and s[idx] == ".":
            idx += 1
            while idx < len(s) and s[idx].isdigit():
                judgeDigit = True
                idx += 1
        # judge e(+/-e234)
        if idx < len(s) and s[idx].lower() == "e" and judgeDigit:
            idx += 1
            if idx < len(s) and (s[idx] == "+" or s[idx] == "-"):
                idx += 1
            judgeDigit = False
            while idx < len(s) and s[idx].isdigit():
                judgeDigit = True
                idx += 1
        # space
        while idx < len(s) and s[idx] == " ":
            idx += 1
        if judgeDigit and idx == len(s):
            return True
        return False
            
