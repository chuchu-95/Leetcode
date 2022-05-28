# class Solution:
#     def maxProfit(self, prices) -> int:
#         # divide prices into two parts, first buy and second buy
#         # the element of arrays is max one
#         firstBuy = [0] * len(prices)
#         secondBuy = [0] * len(prices)
#         # first
#         minPrice = prices[0]
#         for i in range(1, len(prices)):
#             firstBuy[i] = max(firstBuy[i-1], prices[i]-minPrice)
#             minPrice = min(minPrice, prices[i])
#         # second
#         maxPrice = prices[-1]
#         for j in range(len(prices)-2, -1, -1):
#             secondBuy[j] = max(secondBuy[j+1], maxPrice-prices[j])
#             maxPrice = max(maxPrice, prices[j])
#         # sum
#         for idx in range(len(prices)):
#             secondBuy[idx] += firstBuy[idx]
#         return max(secondBuy)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp 
        # n = len(prices)
        # state = [[[0, float("-inf")] for _ in range(3) ] for _ in range(n+1)]
        # for i, price in enumerate(prices):
        #     state[i+1][2][0] = max(state[i][2][0], state[i][2][1]+price)
        #     state[i+1][2][1] = max(state[i][2][1], state[i][1][0]-price)
        #     state[i+1][1][0] = max(state[i][1][0], state[i][1][1]+price)
        #     state[i+1][1][1] = max(state[i][1][1], -price)
        # return state[n][2][0]

        T2_none = 0
        T2_have = float("-inf")
        T1_none = 0
        T1_have = float("-inf")
        for i, price in enumerate(prices):
            T2_none = max(T2_none, T2_have + price)
            T2_have = max(T2_have, T1_none - price)
            T1_none = max(T1_none, T1_have + price)
            T1_have = max(T1_have, -price)
        return T2_none