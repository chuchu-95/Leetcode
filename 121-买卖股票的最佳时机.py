# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         #dp
#         state = [0] * len(prices)
#         minPrice = prices[0]
#         for i in range(1,len(prices)):
#             state[i] = max(state[i-1], prices[i]-minPrice)
#             minPrice = min(minPrice, prices[i])
#         return state[-1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp
        # T[i][k][0] = max{T[i-1][k][0], T[i-1][k][1] + prices[i]}
        # T[i][k][1] = max{T[i-1][k][1], T[i-1][k][0] - prices[i]}
        # n = len(prices)
        # state = [[0, float("-inf")]] * (n+1)
        # for i, price in enumerate(prices):
        #     state[i+1][0] = max(state[i][0], state[i][1]+price)
        #     state[i+1][1] = max(state[i][1], -price)
        # return state[n][0]

        T_none = 0
        T_have = -prices[0]
        for price in prices[1: ]:
            T_none = max(T_none, T_have + price)
            T_have = max(T_have, -price)
        return T_none
        