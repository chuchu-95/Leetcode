class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.helper(nums, [], 0, True, res)
        return res
    def helper(self, nums, sub, start, judge, res):
        res.append(sub)
        for i in range(start, len(nums)):
            if nums[i-1] == nums[i] and start != i:
                continue
            self.helper(nums, sub+[nums[i]], i+1, judge, res)
