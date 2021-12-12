class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        maxArea = 0
        heights = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            maxArea = max(maxArea, self.largestRectangleArea(heights))
        return maxArea
    def largestRectangleArea(self, hts):
        largeArea = 0
        if sum(hts) == 0:
            return 0
        stack = []
        curr = 0
        rect = 0
        left = 0
        right = 0
        while curr < len(hts):
            if stack == [] or hts[stack[-1]] <= hts[curr]:
                stack.append(curr)
                curr += 1
            else:
                rect = stack.pop()
                while stack !=[] and hts[stack[-1]] == hts[rect]:
                    rect = stack.pop()
                if stack == []:
                    left = -1
                else:
                    left = stack[-1]
                right = curr
                largeArea = max(largeArea, (right-left-1)*hts[rect])
        right = curr
        while stack != []:
            rect = stack.pop()
            if stack == []:
                left = -1
            else:
                left = stack[-1]
            largeArea = max(largeArea, (right-left-1)*hts[rect])
        return largeArea
                    