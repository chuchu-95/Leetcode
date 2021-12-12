# 取出第一个单词中的所有字母组成集合，
# 然后考察该集合中的字母在每个单词中出现过的最小次数。
def commonChars(A):
    res = []
    fir = set(A[0])
    for i in fir:
        re = [j.count(i) for j in A]
        min_i = min([j.count(i) for j in A])
        res += min_i*i
    return res
print(commonChars(["bella","label","roller" ]))
