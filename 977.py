def sortedSquares(A):
    l = []
    for i in A:
        l.append(i**2)
    return sorted(l)


print(sortedSquares([-4,-1,0,3,10]))

