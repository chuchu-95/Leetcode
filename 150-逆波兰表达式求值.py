class Solution:   
    def evalRPN(self, tokens) -> int:
        numStack = [] 
        idx = 0
        while idx < len(tokens):
            cur = tokens[idx]
            if self.isOperator(cur):
                operator = cur
                n2 = numStack.pop()
                n1 = numStack.pop()
                subRes = 0
                subRes = self.calculate(int(n1), int(n2), operator)
                numStack.append(str(subRes))
            else:
                numStack.append(cur)
            idx += 1
        res = int(numStack.pop())
        return res
    
    def calculate(self, num1, num2, oper):
        result = 0
        if oper == "+":
            result = num1 + num2
        elif oper == "-":
            result = num1 - num2
        elif oper == "*":
            result = num1 * num2
        elif oper == "/":
            result = int(num1 / num2)
        return result
    
    def isOperator(self, o):
        if o == "+" or o == "-" or o == "*" or o == "/":
            return True
        return False

