class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low+1 < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid
        if target <= nums[low]:
            return low
        elif target <= nums[high] and target > nums[low]:
            return high
        elif target > nums[high]:
            return high + 1