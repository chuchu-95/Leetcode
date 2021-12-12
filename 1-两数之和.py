def twoSum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        result = target - num
        if num in dic:
            return [dic[num], i]
        else:
            dic[result] = i


print(twoSum([2, 7, 11, 15], 9))
