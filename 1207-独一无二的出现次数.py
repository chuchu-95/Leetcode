def uniqueOccurrences(arr):
    dic = {}
    for i in arr:
        dic[i] = dic.get(i,0)+1
    c = [k for k in dic.values()]
    if len(set(c)) == len(c):
        return True
    else:
        return False

print(uniqueOccurrences([1,2,2,1,1,3]))


