class Solution:
    def maxProfit(self, prices) -> int:
        # if increase, buy it
        sum = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i-1]
            if profit < 0:
                continue
            else:
                sum += profit
        return sum