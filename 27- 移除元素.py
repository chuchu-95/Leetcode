# def remove(nums, val):
#     for i in nums[::-1]:
#         if i == val:
#             nums.remove(i)
#         return nums

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = -1
        point = 0
        while point < len(nums):
            if nums[point] != val:
                length += 1
                nums[length] = nums[point]
            point += 1 
        return length+1


