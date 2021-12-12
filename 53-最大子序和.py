class Solution:
    def maxSubArray(self, nums) -> int:
        # time complexity: O(n)
        maxToCurr = nums[0]
        maxRes = nums[0]
        if len(nums) == 1:
            return maxRes
        for i in range(1, len(nums)):
            maxToCurr = max(maxToCurr+nums[i], nums[i])
            maxRes =  max(maxRes, maxToCurr)
        return maxRes