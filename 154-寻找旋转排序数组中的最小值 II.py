class Solution:
    def findMin(self, nums) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            pivot = low + (high - low)//2
            if nums[pivot] == nums[high]:
                high -= 1
            elif nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1
        return nums[low]