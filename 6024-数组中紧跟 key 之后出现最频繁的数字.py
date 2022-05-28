class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        import heapq
        dic = {}
        freqHeap = []
        heapify(freqHeap)
        for idx in range(len(nums)-1):
            if nums[idx] == key:
                target = nums[idx+1]
                if target in dic:
                    dic[target] += 1
                else:
                    dic[target] = 1
        for k in dic:
            heappush(freqHeap, (-dic[k], k))
        return freqHeap[0][1]