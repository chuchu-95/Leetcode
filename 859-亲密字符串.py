def buddyStrings(A, B):
    if len(A) != len(B): return False
    if A == B and len(set(A)) != len(A): return True
    else:
        res = []
        for m, n in zip(A, B):
            if m != n:
                res.append([m, n])
            if len(res) > 2:
                return False
        if len(res) == 2 and res[0] == res[1][::-1]:
            return True


print(buddyStrings("ab", "ba"))
