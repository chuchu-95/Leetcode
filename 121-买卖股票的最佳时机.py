class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp
        state = [0] * len(prices)
        minPrice = prices[0]
        for i in range(1,len(prices)):
            state[i] = max(state[i-1], prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
        return state[-1]