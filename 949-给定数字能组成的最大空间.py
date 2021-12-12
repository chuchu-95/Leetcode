def largestTimeFromDigits(A):
    A.sort()
    for i in range(23, -1, -1):
        for j in range(59, -1, -1):
            re = [i//10, i%10, j//10, j%10]
            rs = sorted(re)
            if A == rs:
                return str(re[0]) + str(re[1]) + ":" + str(re[2]) + str(re[3])
    return ""
print(largestTimeFromDigits([1,2,3,4]))
