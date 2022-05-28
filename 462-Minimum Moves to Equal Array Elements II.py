class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # get the median 
        nums.sort()
        move = 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            move += (nums[j] - nums[i])
            i += 1
            j -= 1
        return move