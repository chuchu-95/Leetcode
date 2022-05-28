# class Solution:
#     def maxSubArray(self, nums) -> int:
#         # time complexity: O(n)
#         maxToCurr = nums[0]
#         maxRes = nums[0]
#         if len(nums) == 1:
#             return maxRes
#         for i in range(1, len(nums)):
#             maxToCurr = max(maxToCurr+nums[i], nums[i])
#             maxRes =  max(maxRes, maxToCurr)
#         return maxRes
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # divide and conquer
        resMax = self.helper(0, len(nums)-1, nums)
        return resMax

    def helper(self, left, right, nums):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        leftMax = self.helper(left, mid, nums)
        rightMax = self.helper(mid+1, right, nums)

        leftCross, rightCross = nums[mid], nums[mid+1]
        cross = 0
        for i in range(mid, left-1, -1):
            cross += nums[i]
            leftCross = max(leftCross, cross)
        cross = 0
        for i in range(mid+1, right+1):
           cross += nums[i]
           rightCross = max(rightCross, cross)
        return max(max(leftMax, rightMax), leftCross+rightCross)
        

        