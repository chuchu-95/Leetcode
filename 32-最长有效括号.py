# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         max_sub = 0
#         for i in range(len(s)-1):
#             for j in range(1, len(s)):
#                 sub_s = s[i: j+1]
#                 if self.correct(sub_s):
#                     if j+1 - i > max_sub:
#                         max_sub = j+1-i
#         return max_sub
#     def correct(self, sub_s):
#         stack = []
#         for i in sub_s:
#             if i == "(":
#                 stack.append(i)
#             elif stack != [] and i == ")":
#                 stack.pop()
#             else:
#                 return False
#         if stack == []:
#             return True
#         else:
#             return False
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        left_edge = -1
        index = 0
        max_length = 0
        judge = 0
        while index < len(s):
            if s[index] == "(":
                stack.append([s[index], index])
            elif stack != [] and s[index] == ")":
                stack.pop()
                if stack == []:
                    judge = index - left_edge
                else:
                    judge = index - stack[-1][1]
            elif stack == [] and s[index] == ")":
                left_edge = index
            
            max_length = max(judge, max_length)
            index += 1
        return max_length