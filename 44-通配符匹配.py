class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # time complexity = O(mn)
        # space complexity = O(mn)
        arr = [[False for n in range(len(s)+1)] for n in range(len(p)+1)]
        arr[0][0] = True
        # initialize arr
        for k in range(1, len(p)+1):
            if p[k-1] == "*":
                arr[k][0] = arr[k-1][0]
        # start
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    arr[j][i] = arr[j-1][i-1]
                if p[j-1] == "*":
                    arr[j][i] = arr[j-1][i] or arr[j][i-1]
        return arr[len(p)][len(s)]

