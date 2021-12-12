class Solution:
    def findPeakElement(self, nums):
        if len(nums) < 2:
            return 0
        left = 0
        right = len(nums)-1
        while left < right:
            pivot = left + (right-left)//2
            if nums[pivot] <= nums[pivot+1]:
               left = pivot + 1
            else:
                right = pivot
        return left