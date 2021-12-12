def search(nums, target):
    #di jian de 
    # return nums.index(target) if target in nums else -1

    #logn
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2 
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

print(search(nums = [-1,0,3,5,9,12], target = 90))
