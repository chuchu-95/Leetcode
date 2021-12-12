def bitwiseComplement(N):
    def my_bin(n):
        L = []
        v = 1
        while v <= n // 2:
            v *= 2
        while v > 0:
            if n < v:
                L.append("0")
            else:
                L.append("1")
                n -= v
            v //= 2
        return "".join(L)
    N_bin = my_bin(N)
    li = ""
    for i in N_bin:
        if i == "1":
            li += "0"
        if i == "0":
            li += "1"
    return int(li, 2)

print(bitwiseComplement(5))

