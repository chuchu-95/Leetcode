class Solution:
    def groupAnagrams(self, strs) :
        dic = {}
        for st in strs:
            lst_st = list(st)
            lst_st.sort()
            key = "".join(lst_st)
            if key in dic:
                dic[key] += [st]
            else:
                dic[key] = [st]
        result = []
        for value in dic.values():
            result.append(value)
        return result

