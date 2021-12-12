class Bucket:
        def __init__(self):
            self.maxBuck = 0
            self.minBuck = float('inf')
        def rewrite(self, num):
            self.maxBuck = max(self.maxBuck, num)
            self.minBuck = min(self.minBuck, num)
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # bucket
        numsLen = len(nums)
        if nums == None or numsLen < 2:
            return 0
        if numsLen == 2:
            return abs(nums[0] - nums[1])

        minNum = nums[0]
        maxNum = nums[0]
        for i in nums:
            minNum = min(minNum, i)
            maxNum = max(maxNum, i)
        if minNum == maxNum:
            return 0

        bucketSize = max(1, (maxNum-minNum) // (numsLen-1))
        bucketSum = (maxNum-minNum) // bucketSize + 1
        arr = []
        for l in range(bucketSum):
            arr.append(Bucket())
        
        # add to bucket
        for j in range(numsLen):
            idx = (nums[j]-minNum)//bucketSize
            arr[idx].rewrite(nums[j])
        #final
        res = 0
        preMax = minNum
        for buck in range(len(arr)):
            if arr[buck].maxBuck == 0:
                continue
            res = max(res, arr[buck].minBuck-preMax)
            preMax = arr[buck].maxBuck
        return res