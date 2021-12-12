# class Solution:
#     def trap(self, height: List[int]) -> int:
#         # space complexity = O(n)
#         # approach1: count the volumn of each num
#         left = []
#         for i in range(len(height)):
#             if i == 0:
#                 left.append(0)
#             else:
#                 maxLeftEach = 0
#                 for j in range(0, i):
#                     if height[j] > maxLeftEach:
#                         maxLeftEach = height[j]
#                 left.append(maxLeftEach)
    
#         right = []
#         for m in range(len(height)-1, -1, -1):
#             if m == len(height)-1:
#                 right.append(0)
#             else:
#                 maxRightEach = 0
#                 for n in range(m+1, len(height)):
#                     if height[n] > maxRightEach:
#                         maxRightEach = height[n]
#                 right.append(maxRightEach)
#         right = right[::-1]
#         result = []
#         for index in range(len(height)):
#             minNum = min(left[index], right[index])
#             if height[index] > minNum:
#                 result.append(0)
#             else:
#                 result.append(minNum-height[index])
#         sum = 0
#         for num in result:
#             sum += num
#         return sum
class Solution:
    def trap(self, height: List[int]) -> int:
        # approach2：two points
        # time complexity = O(n)
        # space complexity = O(1)
        leftmost = 0
        rightmost = 0
        left = 0
        right = len(height)-1
        sum = 0
        while left < right:
            leftmost = max(height[left], leftmost)
            rightmost = max(height[right], rightmost)
            if leftmost < rightmost:
                sum += (leftmost - height[left])
                left += 1
            else:
                sum += (rightmost - height[right])
                right -= 1
        return sum

