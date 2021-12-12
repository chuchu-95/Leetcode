class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #O(n)
        stack = []
        maxArea = 0
        # index
        curr = 0
        rect = 0  #hightest area contain itself
        left = 0
        right = 0
        while curr < len(heights):
            if stack == [] or heights[stack[-1]] <= heights[curr]:
                stack.append(curr)
                curr += 1
            else:
                rect = stack.pop()
                while stack != [] and heights[stack[-1]] == heights[rect]:
                    rect = stack.pop()
                if stack == []:
                    left = -1
                else:
                    left = stack[-1]
                right = curr
                maxArea = max(maxArea, (right-left-1)*heights[rect])
        right = curr
        while stack != []:
            rect = stack.pop()
            if stack == []:
                left = -1
            else:
                left = stack[-1]
            maxArea = max(maxArea, (right-left-1)*heights[rect])
        return maxArea