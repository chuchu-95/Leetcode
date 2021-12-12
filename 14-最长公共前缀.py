def longestCommonPrefix(strs):
    if strs == None:
        return ""
    result = ""
    min_str = len(strs[0])
    num = len(strs)
    # for i in strs:
    #     length = len(i)
    #     if length < min_str:
    #         min_str = length
    # print(min_str)
    for j in range(min_str):
        cnt = 0
        while cnt < num-1:
            print(strs[cnt][j], strs[cnt+1][j])
            if strs[cnt][j] == strs[cnt+1][j]:
                cnt += 1
            else:
                return result
        if cnt == num-1:
            result += strs[0][j]
            print(result)
    return result
print(longestCommonPrefix(["","ciair"]))

    







