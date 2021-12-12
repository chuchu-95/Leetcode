# def firstMissingPositive(nums):
#     i = 1
#     while True:
#         if i not in nums:
#             return i
#         i += 1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        MaxNum = 1 << 31
        # turn negative and zero to MaxNum
        for n in range(len(nums)):
            if nums[n] <= 0:
                nums[n] = MaxNum
        # main
        for i in nums:
            absNum = abs(i)
            if absNum <= len(nums):
                nums[absNum-1] = - abs(nums[absNum-1])
        # find the negative num
        for index in range(len(nums)):
            if nums[index] > 0:
                return index + 1
        return len(nums)+1
