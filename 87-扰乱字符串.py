class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def helper(s1, s2):
            if s1 == None or s2 == None or len(s1) != len(s2):
                return False
            if len(s1) == 1 and s1 == s2:
                return True
            s1_sort = sorted(s1)
            s2_sort = sorted(s2)
            if s1_sort != s2_sort:
                return False
            if s1 in cache_map and cache_map[s1][0] == s2:
                return cache_map[s1][1]
            for idx in range(1, len(s1)):
                s1_left = s1[0: idx]
                s1_right = s1[idx: len(s1)]
                if (helper(s1_left,s2[0:idx]) and helper(s1_right,s2[idx: len(s2)])) or (helper(s1_left,s2[len(s2)-idx: len(s2)]) and helper(s1_right, s2[0:len(s2)-idx])):
                    cache_map[s1] = [s2, True]
                    return True
            cache_map[s1] = [s2, False]
            return False
        cache_map = {}
        res = helper(s1, s2)
        return res

        
        