def add_digit(num):
    while num >= 10:
        num = str(num)
        s = 0
        for i in num:
            s = s + int(i)
        num = s
    return num


print(add_digit(38))
