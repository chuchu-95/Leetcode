class Solution:
    def maxProduct(self, nums):
        maxRes = nums[0]
        curMax = nums[0]
        curMin = nums[0]
        for i in range(1, len(nums)):
            tempMax = curMax
            tempMin = curMin
            curMin = min(tempMin*nums[i], tempMax*nums[i], nums[i])
            curMax = max(tempMin*nums[i], tempMax*nums[i], nums[i])
            maxRes = max(maxRes, curMax)
        return maxRes