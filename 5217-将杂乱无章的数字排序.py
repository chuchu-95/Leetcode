class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        import functools
        res = []
        for num in nums:
            # reverse and reflect to mapping
            reflect = 0
            if num == 0:
                reflect = mapping[0]
            else:
                sub = ""
                judge = False
                str_num = str(num)
                for s in str_num:
                    if not judge and s == '0':
                        continue
                    judge = True
                    sub += str(mapping[int(s)])
                reflect = int(sub)
            res.append(reflect)
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = res[i]

        def cmp(a, b):
            if dic[a] > dic[b]:
                return 1
            elif dic[a] < dic[b]:
                return -1
            else:
                return 0
        return sorted(nums, key=functools.cmp_to_key(cmp))