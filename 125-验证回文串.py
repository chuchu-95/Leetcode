class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = s.lower()
        pointA = 0
        pointB = len(s)-1
        while pointA <= pointB:
            while not s[pointA].isalnum():
                pointA += 1
                if pointA == len(s):
                    return True
            while not s[pointB].isalnum():
                pointB -= 1
                if pointB == -1:
                    return True
            if pointA == pointB:
                return True
            if s[pointA] == s[pointB]:
                pointA += 1
                pointB -= 1
            else:
                return False
        return True