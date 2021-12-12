def perfect(n):
    lst = []
    for i in range(1, n//2+1):
        if n % i == 0:
            lst.append(i)
    m = sum(lst)
    if m == n:
        return True
    else:
        return False


print(perfect(9))





