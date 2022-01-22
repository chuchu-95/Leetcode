# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals = self.quickSort(intervals)
#         idx = 1
#         length = len(intervals)
#         while idx < length:
#             if intervals[idx-1][1] >= intervals[idx][0]:
#                 num = max(intervals[idx][1], intervals[idx-1][1])
#                 intervals = intervals[:idx-1]+[[intervals[idx-1][0], num]] + intervals[idx+1:]
#                 length -= 1
#             else:
#                 idx += 1
#         return intervals
#     def quickSort(self, lists):
#         if len(lists) < 2:
#             return lists
#         else:
#             pivot = lists[0]
#             left = []
#             right = []
#             # left = [lst for lst in lists[1:] if lst[0] < pivot[0]]
#             # right = [lst for lst in lists[1:] if lst[0] > pivot[0]]
#             for lst in lists[1:]:
#                 if lst[0] < pivot[0]:
#                     left.append(lst)
#                 elif lst[0] > pivot[0]:
#                     right.append(lst)
#                 else:
#                     if lst[1] <= pivot[1]:
#                         left.append(lst)
#                     elif lst[1] > pivot[1]:
#                         right.append(lst)
#             return self.quickSort(left) + [pivot] + self.quickSort(right)
class Solution:
    def merge(self, intervals):
        idx = 0
        res = []
        start = []
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        while idx < len(intervals):
            st = start[idx]
            while idx < len(intervals)-1 and start[idx+1] <= end[idx]:
                idx += 1
            ed = end[idx]
            res.append([st,ed])
            idx += 1
        return res
            


