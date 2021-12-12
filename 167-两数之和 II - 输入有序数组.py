# class Solution:
#     def twoSum(self, numbers, target: int):
#         dic = {}
#         for idx, num in enumerate(numbers):
#             if num not in dic:
#                 dic[target-num] = idx+1
#             else:
#                 return [dic[num], idx+1]

class Solution:
    def twoSum(self, numbers, target: int):
        for idx1 in range(len(numbers)-1):
            judge = target - numbers[idx1]
            low = idx1+1
            high = len(numbers)-1
            while low <= high:
                mid = low + (high-low)//2
                if numbers[mid] == judge:
                    return [idx1+1, mid+1]
                elif numbers[mid] > judge:
                    high = mid - 1
                else:
                    low = mid + 1
        return [-1,-1]
