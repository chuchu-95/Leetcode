def subtractProductAndSum(n):
    n1 = list(str(n))
    a, b = 1, 0
    for i in n1:
        a *= int(i)
        b += int(i)
    return a-b


print(subtractProductAndSum(234))

