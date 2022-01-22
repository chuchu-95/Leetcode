# class Solution:
#     def canAttendMeetings(self, intervals) -> bool:
#         intervals.sort(key = lambda x: x[0])
#         for i in range(len(intervals)-1):
#             if intervals[i][1] > intervals[i+1][0]:
#                 return False
#         return True

class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        start = []
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        for idx in range(len(intervals)-1):
            if end[idx] > start[idx+1]:
                return False
        return True