def balancedStringSplit(s):
    count = 0
    r_app = 0
    l_app = 0
    for i in s:
        if i == "R":
            r_app += 1
        if i == "L":
            l_app += 1
        if r_app == l_app:
            count += 1
    return count


print(balancedStringSplit("LLLLRRRR"))
