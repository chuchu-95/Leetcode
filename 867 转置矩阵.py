def transpose(A):
    B = []
    for i in range(len(A[0])):
        B.append([0 for j in range(len(A))])
    for i in range(len(A)):
        for j in range(len(A[i])):
            B[j][i] = A[i][j]
    return B


    # B = [[0 for i in range(len(A))]for i in range(len(A[0]))]
    # for i in range(len(A)):
    #     for j in range(len(A[i])):
    #         B[j][i] = A[i][j]
    # return B


    # B = []
    # l = []
    # for i in range(len(A)):
    #     l.append(0)
    # for i in range(len(A[0])):
    #     B.append(l.copy())
    # for i in range(len(A)):
    #     for j in range(len(A[i])):
    #         B[j][i] = A[i][j]
    # return B

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
