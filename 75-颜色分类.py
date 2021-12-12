class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        last = len(nums) - 1
        #initialize
        while first < len(nums):
            if nums[first] == 0:
                first += 1
            else:
                break
        while last > 0:
            if nums[last] == 2:
                last -= 1
            else:
                break
        #start
        idx = first
        while idx < last+1:
            if nums[idx] == 2:
                nums[idx], nums[last] = nums[last], nums[idx]
                last -= 1
            elif nums[idx] == 0:
                nums[idx], nums[first] = nums[first], nums[idx]
                first += 1
                idx = first
            else:
                idx += 1