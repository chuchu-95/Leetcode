class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastLen = 0
        judge = 0
        for st in s:
            if st == " ":
                judge = 1
                continue
            else:
                if judge == 1:
                    lastLen = 0
                    judge = 0
                lastLen += 1
        return lastLen