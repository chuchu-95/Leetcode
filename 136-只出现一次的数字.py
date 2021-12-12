class Solution:
    def singleNumber(self, nums) -> int:
        # ^
        a = 0
        for num in nums:
            a = a ^ num
        return a