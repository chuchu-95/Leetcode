class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections
        import heapq
        res = []
        freqDict = collections.Counter(nums)
        freqHeap = []
        heapify(freqHeap)
        for num in freqDict:
            heappush(freqHeap, (freqDict[num], num))
            if len(freqHeap) > k:
                heappop(freqHeap)

        for sub in freqHeap:
            res.append(sub[1])
        return res