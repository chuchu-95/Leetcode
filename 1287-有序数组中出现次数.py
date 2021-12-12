def findSpecialInteger(arr):
    per = len(arr) * 0.25
    dic = {}
    for i in arr:
        dic[i] = dic.get(i, 0) + 1
    for k in dic.keys():
        if dic[k] > per:
            return k

print(findSpecialInteger([1,1,2,3,3,4,4,8,8]))
