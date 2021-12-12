def isPalindrome(x):
    if x < 0:
        return False
    else:
        x_re = 0
        x_div = x
        while x_div != 0:
            x_re += x_div % 10
            x_re *= 10
            x_div //= 10
        x_re //= 10
        return True if x_re == x else False
print(isPalindrome(121))