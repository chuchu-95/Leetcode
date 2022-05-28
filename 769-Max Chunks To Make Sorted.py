class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt = 0
        border = 0
        for index, num in enumerate(arr):
            border = max(border, num)
            if border == index:
                cnt += 1
        return cnt