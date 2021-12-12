class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper([], 0, nums, res)
        return res
    def helper(self, sub, start, nums, res):
        res.append(sub)
        for idx in range(start, len(nums)):
            self.helper(sub+[nums[idx]], idx+1, nums, res)

