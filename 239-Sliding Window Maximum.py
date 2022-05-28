class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque()
        res = []
        for idx, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(idx)
            if idx - queue[0] + 1 > k:
                queue.popleft()
            if idx >= k-1 :
                res.append(nums[queue[0]])
        return res