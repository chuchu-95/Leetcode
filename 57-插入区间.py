class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        idx = 0
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            result.append(intervals[idx])
            idx += 1
        if idx == len(intervals):
            result.append(newInterval)
            return result
        left = min(intervals[idx][0], newInterval[0])

        right = newInterval[1]
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            idx += 1
            right = max(intervals[idx-1][1], newInterval[1])
        result.append([left, right])

        while idx < len(intervals):
            result.append(intervals[idx])
            idx += 1
        return result