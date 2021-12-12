def isMatch(s, p):
    # build array len(s)+1, len(p)+1
    arr = [[False for q in range(len(s)+1)] for q in range(len(p)+1)]
    arr[0][0] = True
    # initialize s(none) 
    for k in range(1, len(p)+1):
        if p[k-1] == "*":
            arr[k][0] = arr[k-2][0]

    # start
    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if s[i-1] == p[j-1] or p[j-1] == ".": 
                arr[j][i] = arr[j-1][i-1]
            elif p[j-1] == "*":
                if p[j-2] == "." or p[j-2] == s[i-1]:
                    arr[j][i] = arr[j-2][i] or arr[j][i-1] 
                else:  
                    arr[j][i] = arr[j-2][i] 
    print(arr)      
    return arr[len(p)][len(s)]
print(isMatch("aa", "a*"))
