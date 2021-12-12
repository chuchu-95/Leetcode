class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = ""
        each = [None] * n
        each[0] = 1
        nums = []
        for n in range(1, n+1):
            nums.append(n)
        # nums = [1,2,3,4]
        for i in range(1, n):
            each[i] = each[i-1] * i
        k -= 1 # index start from 0
        for cnt in range(n-1, 0, -1):
            idx = k // each[cnt]
            sub = str(nums.pop(idx))
            result += sub
            k %= each[cnt]
        result += str(nums[0])
        return result


        

