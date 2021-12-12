class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        cnt = 0
        length = len(needle)
        if needle == "":
            return 0
        for i in range(len(haystack)-length+1):
            if haystack[i: i+length] == needle:
                return i
        return -1