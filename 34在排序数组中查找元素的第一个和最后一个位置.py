class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        if nums == []:
            return [-1,-1]
        # find start point
        left = 0
        right = len(nums)-1
        while left+1 < right:
            mid = (left+right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        sp = -1
        if nums[left] == target:
            sp = left
        elif nums[right] == target:
            sp = right
        if sp == -1:
            return [-1, -1]
        # find last point
        left = 0
        right = len(nums)-1
        while left+1 < right:
            mid = (left+right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        lp = -1
        #[a,a]consider last, judge right first
        if nums[right] == target:
            lp = right
        elif nums[left] == target:
            lp = left
        result += [sp, lp]
        return result