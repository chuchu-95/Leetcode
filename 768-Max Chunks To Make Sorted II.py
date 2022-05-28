class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        arr_sorted = sorted(arr)
        sum1, sum2 = 0, 0
        for i, j in zip(arr, arr_sorted):
            sum1 += i
            sum2 += j
            if sum1 == sum2:
                res += 1
        return res