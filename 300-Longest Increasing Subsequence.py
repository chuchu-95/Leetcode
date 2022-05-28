# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # dp
#         n = len(nums)
#         state = [1 for i in range(n)]
#         for i in range(1, n):
#             for j in range(0, i):
#                 if nums[i] > nums[j]:
#                     state[i] = max(state[i], state[j] + 1)
#         return max(state)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # greedy
        sub = []
        for num in nums:
            if len(sub) != 0 and sub[-1] >= num:
                # binary search
                left, right = 0, len(sub)-1
                while left < right:
                    mid = left + (right-left)//2
                    if sub[mid] < num:
                        left = mid + 1
                    else:
                        right = mid 
                sub[left] = num
            else:
                sub.append(num)
        return len(sub)