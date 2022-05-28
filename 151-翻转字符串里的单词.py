# class Solution:
#     def reverseWords(self, s: str) -> str:
#         res = ""
#         sLen = len(s)
#         start = sLen - 1
#         end = sLen - 1
#         while start > -1 and end > -1:
#             if s[end].isalnum():
#                 start = end
#                 while s[start-1] != " " and start != 0:
#                     start -= 1
#                 res += (s[start: end+1] + " ")
#                 end = start - 1
#             else:
#                 end -= 1
#         return res[:-1]

class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s)
        n = len(words)
        # reverse whole
        self.reverseWord(words, 0 ,n-1)
        # reverse single
        self.reverseEach(words, 0, 0)
        # delete space
        return "".join(self.deleteSpace(words, 0, 0))
        
    def reverseWord(self,arr, i, j):
        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
            
    def reverseEach(self, arr, i, j):
        n = len(arr)
        while i < n:
            while i < j:
                i += 1
            while i < n and arr[i] == " ":
                i += 1
            while j < i:
                j += 1
            while j < n and arr[j] != " ":
                j += 1
            self.reverseWord(arr, i, j-1)
    
    def deleteSpace(self, arr, i, j):
        n = len(arr)
        while j < n:
            while j < n and arr[j] == " ":
                j += 1
            while j < n and arr[j] != " ":
                arr[i] = arr[j]
                i += 1
                j += 1
            while j < n and arr[j] == " ":
                j += 1
            if j < n:
                arr[i] = " "
                i += 1
        return arr[0: i]
        