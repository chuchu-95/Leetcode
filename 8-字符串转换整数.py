def myAtoi(s):
    # ascii ord
    result = 0
    judge = 1
    sign = 1
    for i in s:
        ascii_i = ord(i)
        str_i = str(ascii_i - ord("0"))
        # num have not appear
        if judge == 1:
            if i == " ":
                continue
            elif i == "-":
                judge = 0
                sign = -1
            elif i == "+":
                judge = 0
            elif str_i == i:
                judge = 0
                result += int(i)
                result *= 10
            else:
                break
        # first num appear
        elif judge == 0:
            if str_i == i:
                result += int(i)
                result *= 10
            else:
                break
    result //= 10
    a = -(1 << 31)
    b = (1 << 31) - 1
    if  result < a or result > b:
        return a if sign == -1 else b
    return  result * sign

print(myAtoi("+1444"))