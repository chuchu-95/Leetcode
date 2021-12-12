# out of time
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         eachMin = [0 for m in range(len(nums))]
#         for i in range(1, len(nums)):
#             for j in range(0, i):
#                 if i <= nums[j]+j:
#                     if eachMin[i] == 0:
#                         eachMin[i] = eachMin[j] + 1
#                     eachMin[i] = min(eachMin[i], eachMin[j] + 1)
#         return eachMin[-1]
class Solution:
    def jump(self, nums: List[int]) -> int:
        # O(n)
        if nums == [] or len(nums) == 1:
            return 0
        idx = 0
        step = 0
        curMax = 0
        nextMax = 0
        # judge whether the given array is valid(while True)
        while idx <= nextMax:
            while idx <= curMax:
                nextMax = max(nums[idx]+idx, nextMax)
                idx += 1
            step += 1
            curMax = nextMax
            if nextMax >= len(nums)-1 :
                return step
        return 0