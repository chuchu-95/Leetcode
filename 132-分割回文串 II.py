class Solution:
    def minCut(self, s: str) -> int:
        sLen = len(s)
        cut = [0] * (sLen+1)
        # initialize cut of each subStr's max cut
        for c in range(sLen+1):
            cut[c] = c - 1
        #str =      a  b  a  d  d
        #cut = [-1, 0, 1, 2, 3, 4]
        #cutIdx =   1  2  3  4  5

        #start
        #external i: the center of palindrome
        for i in range(sLen):
            #internal j: the radius of i ----> [i-j] i [i+j]
            # odd and sole num
            j = 0
            while j <= i and i+j < sLen and s[i-j] == s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j])
                j += 1 
            # even
            j = 1
            while j <= i+1 and i+j < sLen and s[i-j+1] == s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j+1])    
                j += 1
        return cut[-1]