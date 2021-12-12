class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        judge = [False for n in range(len(nums))]
        nums.sort()
        self.dfsHelper(len(nums), result, [], nums, judge)
        return result
    def dfsHelper(self,end, result, subList, nums, judge):
        if len(subList) == len(nums):
            result.append(subList)
        else:
            for i in range(end):
                if i > 0 and nums[i-1] == nums[i] and judge[i-1] != True:
                    continue
                elif judge[i] != True:
                    judge[i] = True
                    self.dfsHelper(end, result, subList+[nums[i]], nums, judge)
                    judge[i] = False