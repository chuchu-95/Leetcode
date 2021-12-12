def repeatedNTimes(A):
    A.sort()
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            return A[i]


print(repeatedNTimes([1,2,3,3]))

