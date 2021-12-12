class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        reachIndex = 0
        i = 0
        while i < len(nums) and i <= reachIndex:
            reachIndex = max(reachIndex, i+nums[i])
            i += 1
            if reachIndex >= len(nums)-1:
                return True
        return False