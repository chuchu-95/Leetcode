class Solution:
    def minMeetingRooms(self, intervals) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        roomNum = 1
        startIdx = 0
        endIdx = 0
        while startIdx < len(intervals):
            while startIdx < len(intervals)-1 and end[endIdx] > start[startIdx+1]:
                roomNum += 1
                startIdx += 1
            endIdx += 1
            startIdx += 1

        return roomNum