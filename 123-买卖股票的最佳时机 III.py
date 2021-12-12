class Solution:
    def maxProfit(self, prices) -> int:
        # divide prices into two parts, first buy and second buy
        # the element of arrays is max one
        firstBuy = [0] * len(prices)
        secondBuy = [0] * len(prices)
        # first
        minPrice = prices[0]
        for i in range(1, len(prices)):
            firstBuy[i] = max(firstBuy[i-1], prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
        # second
        maxPrice = prices[-1]
        for j in range(len(prices)-2, -1, -1):
            secondBuy[j] = max(secondBuy[j+1], maxPrice-prices[j])
            maxPrice = max(maxPrice, prices[j])
        # sum
        for idx in range(len(prices)):
            secondBuy[idx] += firstBuy[idx]
        return max(secondBuy)

