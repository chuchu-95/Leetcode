# def longestPalindrome(s):
#     max_length = 0
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             if judge_reverse_new(s[i: j+1]):
#                 substring = s[i: j+1]
#                 sub_len = len(substring)
#                 if sub_len > max_length:
#                     max_length = sub_len
#                     substring_max = substring
#     return substring_max

# def judge_reverse(s):
#     if len(s) < 2:
#         return True
#     if s[0] == s[-1]:
#         return judge_reverse(s[1: -1])
#     else:
#         return False

# def judge_reverse_new(s):
#     point1 = 0
#     point2 = len(s)-1
#     while point1 != point2 and point1-point2 != 1:
#         if s[point1] == s[point2]:
#             point1 += 1
#             point2 -= 1
#         else:
#             return False
#     return True

def longestPalindrome(s):
    length = len(s)
    max_length = 0
    point1, point2 = 0, 0
    for i in range(length):
        lenChar = spreadChar(s, i, i)
        lenNull = spreadChar(s, i, i+1)
        max_length = max(lenChar, lenNull)
        if max_length > point2 - point1:
            point1 = i - (max_length - 1)//2
            point2 = i + max_length//2
    return s[point1 : point2+1]


def spreadChar(s, point1, point2):
    while point1 >= 0 and point2 < len(s) and s[point1]==s[point2]:
        point1 -= 1
        point2 += 1
    return point2 - point1 - 1

print(spreadChar("bbsd", 0, 1))
print(longestPalindrome("abbada"))