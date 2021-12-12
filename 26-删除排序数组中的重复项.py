# def removeDuplicates(nums):
#     m = 0
#     for i in nums:
#         if nums[m] != i:
#             m += 1
#             nums[m] = i
#     return m + 1


# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         length = 0
#         point = 0
#         while point < len(nums):
#             point += 1
#             length += 1
#             while point < len(nums) and nums[point-1] == nums[point]:
#                 nums.pop(point)
#         return length

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        point = 0
        while point < len(nums):
            if nums[length] != nums[point]:
                length += 1
                nums[length] = nums[point]
            point += 1
        return length+1

