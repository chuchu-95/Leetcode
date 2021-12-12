class Solution:
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1
        if nums[low] <= nums[high]:
            return nums[0]
        while low < high:
            pivot = low + (high-low)//2
            if nums[pivot] > nums[high]:
                low = pivot + 1
            elif nums[pivot] < nums[high]:
                high = pivot
        return nums[low]
