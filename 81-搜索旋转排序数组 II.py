class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1
        while low <= high:
            while low <= high and nums[low] == nums[high]:
                high -= 1
            mid = low + (high-low)//2
            if target == nums[mid]:
                return True
            if nums[mid] >= nums[low]:
                if target < nums[mid] and target >= nums[low]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
            
        if nums[low] == target or nums[high] == target:
            return True
        return False