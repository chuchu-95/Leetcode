def moveToRight(lst, left):
    while left == 0 or (left < len(lst) and lst[left-1] == lst[left]):
        left += 1
    return left
def moveToLeft(lst, right):
    while right == len(lst)-1 or (right >= 0 and lst[right] == lst[right+1]):
        right -= 1
    return right

def threeSum(nums):
    leth = len(nums)
    i = 0
    result = []
    nums.sort()
    while i < leth-2:
        base = nums[i]
        left = i + 1
        right = leth - 1
        while left < right:
            sum = base + nums[left] + nums[right]
            if sum == 0:
                result.append([nums[base], nums[left], nums[right]])
                left = moveToRight(nums, left+1)
                right = moveToLeft(nums, right-1)
            elif sum > 0:
                right = moveToLeft(nums,right-1)
            else:
                left = moveToRight(nums, left+1)
        i = moveToRight(nums, i+1)
    return result
print(threeSum([-1,0,1]))

