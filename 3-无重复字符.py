def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # if s == "":
    #     return 0
    # else:
    #     str_longest = []
    #     for i in range(len(s)):
    #         cnt = 1
    #         for j in range(i+1, len(s)):
    #             str_skip = s[i: j+1]
    #             set_skip = set(str_skip)
    #             if len(str_skip) != len(set_skip):
    #                 break
    #             else:
    #                 cnt += 1
    #         str_longest.append(cnt)
    #     return max(str_longest)
    
    max_length = 0
    point = 0
    dic = {}
    for i, emt in enumerate(s):
        if emt in dic:
            point = max(dic[emt]+1, point)
            dic[emt] = i
            max_length = max(max_length, i-point+1)
        else:
            dic[emt] = i
            max_length = max(max_length, i - point + 1)
    return max_length
        
            

print(lengthOfLongestSubstring("abcdbcbb"))
