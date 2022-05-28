class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memoryDict = {}
        def count(idx, rest_k, pre_char, pre_cnt):   
            cur = str(idx) + " " + str(rest_k) + " " + pre_char + " " + str(pre_cnt)
            if cur in memoryDict:
                return memoryDict[cur]
            # must firstly judge
            # impossible condition(only happen to delete)
            if rest_k < 0:
                return float('inf')

            # when to break
            if idx+rest_k >= len(s):
                return 0

            if s[idx] == pre_char:
                carry = 1 if pre_cnt == 1 or pre_cnt == 9 or pre_cnt == 99 else 0
                res = carry + count(idx+1, rest_k, s[idx], pre_cnt+1)
                memoryDict[cur] = res
            else:
                #delete
                cnt_del = count(idx+1, rest_k-1, pre_char, pre_cnt)
                #reserve
                cnt_rev = 1 + count(idx+1, rest_k, s[idx], 1)
                res = min(cnt_del, cnt_rev)
                memoryDict[cur] = res
            return res
        return count(0, k, "", 0)
