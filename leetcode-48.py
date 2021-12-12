def secondHighest(s):
    # ascii ord
    res = []
    for i in s:
        ascii_i = ord(i)
        if ascii_i >= ord("0") and ascii_i <= ord("9"):
            res.append(int(i))
    res_single = list(set(res))
    if len(res_single) > 1:
        res_single.sort()
        return res_single[-2]
    return -1
# print(secondHighest("dfa12321afd"))

def sumlist(arr):
    result = [[]]
    for i in arr:
        result += [j + [i] for j in result]
    return result


def getMaximumConsecutive(coins):
    coins.sort()
    arr = sumlist(coins)
    cnt = 0
    i = 1
    while i < len(arr)-1:
        while sum(arr[i-1]) == sum(arr[i]):
            i += 1
        if sum(arr[i]) == cnt+1:
            cnt += 1
        i += 1
    return cnt+1
print(getMaximumConsecutive([1,2,4]))