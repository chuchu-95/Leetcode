class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        p1 = 0
        p2 = 0
        vLen1 = len(ver1)
        vLen2 = len(ver2)
        while p1 < vLen1 and p2 < vLen2:
            cur1 = ver1[p1]
            cur2 = ver2[p2]
            start1 = 0
            start2 = 0
            # delete forward 0
            start1 = self.removePreZero(cur1, start1)
            start2 = self.removePreZero(cur2, start2)
            # compare
            if int(cur1[start1:]) > int(cur2[start2:]):
                return 1
            elif int(cur1[start1:]) < int(cur2[start2:]):
                return -1
            else:
                p1 += 1
                p2 += 1
        while p1 < vLen1:
            c1 = ver1[p1]
            s1 = self.removePreZero(c1, 0)
            if c1[s1:] != "0":
                return 1
            p1 += 1
        while p2 < vLen2:
            c2 = ver2[p2]
            s2 = self.removePreZero(c2, 0)
            if c2[s2:] != "0":
                return -1
            p2 += 1
        return 0

    def removePreZero(self, str, first):
        if len(str) > 1:
            while first < len(str) and str[first] == '0':
                first += 1
        if first == len(str):
            first = len(str) - 1
        return first

