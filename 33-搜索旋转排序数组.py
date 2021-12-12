class Solution:
    def search(self, nums, target: int) -> int:
        point1 = 0
        point2 = len(nums) - 1
        while point1 <= point2:
            index = (point1+point2) // 2
            if nums[index] == target:
                return index
            if nums[index] >= nums[point1]:
                if target >= nums[point1] and target < nums[index]:
                    point2 = index-1
                else:
                    point1 = index+1
            else:
                if target <= nums[point2] and target > nums[index]:
                    point1 = index+1
                else:
                    point2 = index-1
        return -1

