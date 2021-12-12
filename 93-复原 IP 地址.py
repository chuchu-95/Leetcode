class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        if len(s) == 0 or len(s) > 12 or len(s) < 4:
            return result
        self.helper("", s, result, 0)
        return result
    def helper(self, part, s, result, plen):
        if plen == 4 and len(s) == 0:
            result.append(part[1:])
        if plen == 4 or len(s) == 0:
            return
        else:
            #cut 1
            self.helper(part+"."+s[0:1], s[1:], result, plen+1)
            #cut 2
            if len(s) > 1 and s[0] != '0' :
                self.helper(part+"."+s[0:2], s[2:], result, plen+1)
                #cut 3
            if len(s) > 2 and s[0] != '0' and int(s[0:3]) <= 255:
                self.helper(part+"."+s[0:3], s[3:], result, plen+1)