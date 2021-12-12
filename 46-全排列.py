class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        judge = [False for n in range(len(nums))]
        self.dfsHelper(result, len(nums), [], nums, judge)
        return result
    def dfsHelper(self,result, length, subList, nums, judge):
        if len(subList) == length:
            result.append(subList)
        else:
            for i in range(length):
                if judge[i] != True:
                    judge[i] = True
                    self.dfsHelper(result, length, subList+[nums[i]], nums, judge)
                    judge[i] = False