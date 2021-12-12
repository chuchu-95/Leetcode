# def reverse(x):
#     x_re = abs(x)
#     m = int(str(x_re)[::-1])
#     if -2**31 < m < 2**31-1:
#         return m if x > 0 else -m
#     else:
#         return 0

# def reverse(x):
#     x_abs = abs(x)
#     length = len(str(x_abs)) 
#     x_re = 0
#     for i in range(length):
#         sp = x_abs // (10**(length-1))
#         x_abs = x_abs % (10**(length-1))
#         sp_num = sp * (10**i)
#         x_re += sp_num
#         length -= 1
#     if x_re <= -2**31 or x_re >= 2**31:
#         return 0
#     return x_re if x > 0 else -x_re

def reverse(x):
    x_abs = abs(x)
    x_re = 0
    while x_abs != 0:
        last = x_abs % 10
        x_abs = x_abs // 10
        x_re += last
        x_re *= 10
    x_re = x_re // 10
    a = -(1 << 31)
    b = (1 << 31) - 1
    if  x_re < a or x_re > b:
        return 0
    return x_re if x > 0 else -x_re

print(reverse(1534236469))
