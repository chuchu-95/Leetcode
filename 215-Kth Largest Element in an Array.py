class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # priority queue
        import heapq
        priQueue = []
        heapify(priQueue)
        for n in nums:
            heappush(priQueue, n)
            if len(priQueue) > k:
                heappop(priQueue)
        return priQueue[0]