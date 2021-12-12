class Solution:
    def singleNumber(self, nums) -> int:
        # bit operation
        ans = 0
        for i in range(32):
            currentBitSum = 0
            for num in nums:
                currentBitSum += ((num >> i) & 1)
            if currentBitSum % 3 != 0:
                #judge if answer is negative number
                if i == 31:
                    ans -= (1 << i)                   
                else:
                    ans |= (1 << i)
        return ans
