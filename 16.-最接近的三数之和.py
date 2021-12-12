def threeSumClosest(self, nums: List[int], target: int) -> int:
    close_dict = {}
    length = len(nums)
    nums.sort()
    i = 0
    while i < length-2:
        base = nums[i]
        left, right = i+1, length-1
        while left < right:
            sum = base + nums[left] + nums[right]
            if sum == target:
                return target
            elif sum > target:
                right -= 1
            else:
                left += 1
                if nums[left-1] == nums[left]:
                    left += 1
            close_dict[abs(target-sum)] = sum

        if nums[i] == nums[i+1]:
            i += 1
        i += 1
    close = min(close_dict.keys())
    return close_dict[close]