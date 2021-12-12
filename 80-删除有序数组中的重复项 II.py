class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        p_fix = 2
        p_move = 2
        while p_move < len(nums):
            if nums[p_move] != nums[p_fix-2]:
                nums[p_fix] = nums[p_move]
                p_fix += 1
            p_move += 1
        return p_fix 
            