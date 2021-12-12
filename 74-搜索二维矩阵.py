class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        left = 0
        right = len(matrix)- 1
        while left <= right:
            mid = left + (right-left)//2
            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                return True
        lt = 0
        rt = len(matrix[right]) - 1
        while lt <= rt:
            md = lt + (rt-lt)//2
            if matrix[right][md] < target:
                lt = md + 1
            elif matrix[right][md] > target:
                rt = md - 1
            else:
                return True
        return False