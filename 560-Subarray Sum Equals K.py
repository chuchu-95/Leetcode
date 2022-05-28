class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum, res = 0, 0
        mapFreq = {}
        mapFreq[0] = 1
        for num in nums:
            curSum += num
            if curSum - k in mapFreq:
                res += mapFreq[curSum-k]
            if curSum in mapFreq:
                mapFreq[curSum] += 1
            else:
                mapFreq[curSum] = 1
        return res