# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         if len(triangle) == 1:
#             return triangle[0][0]
#         # create num list
#         count = []
#         for i in range(len(triangle)):
#             count.append([])
#             for j in range(len(triangle[i])):
#                 count[i].append(math.pow(10,4)+1)
#         #count = [[0], [0,0], [0,0,0],[0,0,0,0]]
#         # initialize
#         count[0][0] = triangle[0][0]
#         for row in range(len(triangle)-1):
#             for idx in range(len(triangle[row])):
#                 count[row+1][idx] = min(count[row+1][idx],count[row][idx] + triangle[row+1][idx])
#                 count[row+1][idx+1] = min(count[row+1][idx+1],count[row][idx] + triangle[row+1][idx+1])
#         return min(count[-1])


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # O(n)
        last = [0] * len(triangle)
        last[0] = triangle[0][0]
        for row in range(1, len(triangle)):
            last[row] += last[row-1]
            for idx in range(len(triangle[row])):
                if idx == 0 or idx == len(triangle)-1:
                    temPre = last[idx]
                    last[idx] += triangle[row][idx]
                else:
                    a = last[idx]
                    last[idx] = min(triangle[row][idx]+last[idx], triangle[row][idx] + temPre)
                    temPre = a
        return min(last)

