class Solution:
    def calculate(self, s: str) -> int:
        sign, num, stack = "+", 0, []
        for idx in range(len(s)):
            if s[idx].isdigit():
                num = num*10 + int(s[idx])
            if s[idx] in "+-*/" or idx == len(s)-1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                sign = s[idx]
                num = 0
        return sum(stack)