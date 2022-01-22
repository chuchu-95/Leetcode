class MedianFinder:
    import heapq

    def __init__(self):
        self.leftMax = list()
        self.rightMin = list()
        heapify(self.leftMax)
        heapify(self.rightMin)


    def addNum(self, num: int) -> None:
        left = self.leftMax
        right = self.rightMin 
        # add then turn to odd
        if len(left) == len(right):
            if len(right) == 0:
                heappush(left, -num)
            else:
                if num <= right[0]:
                    heappush(left, -num)
                else:
                    temp = heappop(right)
                    heappush(left, -temp)
                    heappush(right, num)
        # add then turn to even
        else:
            if num >= -left[0]:
                heappush(right, num)
            else:
                temp = heappop(left)
                heappush(right, -temp)
                heappush(left, -num)

    def findMedian(self) -> float:
        left = self.leftMax
        right = self.rightMin
        if len(left) == len(right):
            return (-left[0]+right[0]) / 2
        else:
            return -left[0]




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()