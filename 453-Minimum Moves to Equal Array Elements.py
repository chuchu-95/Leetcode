class Solution:
    def minMoves(self, nums) -> int:
        sum_nums = sum(nums)
        min_num = min(nums)
        len_nums = len(nums)
        return sum_nums - min_num*len_nums
        