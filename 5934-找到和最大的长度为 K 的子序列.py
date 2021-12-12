class Solution:
    def maxSubsequence(self, nums, k: int):
        numsDummy = list(nums)
        nums.sort()
        negIdx = 0
        for idx, n in enumerate(nums):
            if n >= 0:
                negIdx = idx
                break
        end = len(nums)
        judge = end - negIdx
        choose = []
        if judge < k:
            choose = nums[negIdx-(k-judge):negIdx] + nums[negIdx:]
        else:
            choose = nums[end-k:]
        res = []
        for i in numsDummy:
            if i in choose:
                res.append(i)
                choose.remove(i)
        
        return res