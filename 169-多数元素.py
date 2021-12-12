# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         dic = {}
#         for i in nums:
#             if i not in dic:
#                 dic[i] = 1
#             else:
#                 dic[i] += 1
#         pivot = len(nums) / 2
#         for k in dic:
#             if dic[k] > pivot:
#                 return k

