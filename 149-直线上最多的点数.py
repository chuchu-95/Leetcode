class Solution:
    def maxPoints(self, points) -> int:
        if len(points) <= 2:
            return len(points)
        res = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                y = points[i][1]-points[j][1]
                x = points[i][0]-points[j][0]
                cnt = 2
                for p in range(j+1, len(points)):
                    pY = points[p][1] - points[i][1]
                    pX = points[p][0] - points[i][0]
                    if pY * x == pX * y:
                        cnt += 1
                res = max(res, cnt)
        return res