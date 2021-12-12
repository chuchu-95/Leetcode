def fourSum(nums, target):
    length = len(nums)
    result = []
    nums.sort()
    index = 0
    while index < length-3:
        first = nums[index]
        i = index + 1
        while i < length - 2:
            second = nums[i]
            left, right = i+1, length-1
            while left < right:
                sum = first + second + nums[left] + nums[right]
                if sum == target:
                    result.append([first, second, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                elif sum > target:
                    right -= 1
                else:
                    left += 1
                    if nums[left-1] == nums[left]:
                        left += 1
            i += 1
            while i < length-2 and nums[i-1] == nums[i]:
                i += 1
        index += 1
        while index < length-3 and nums[index-1] == nums[index]:
            index += 1
    return result         

print(fourSum([0,0,0,0,4,-2,-3,-3,-3,-2,-2,-3], -1))