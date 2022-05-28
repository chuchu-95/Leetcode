# class Solution:
#     def maxProfit(self, prices) -> int:
#         # if increase, buy it
#         sum = 0
#         for i in range(1, len(prices)):
#             profit = prices[i] - prices[i-1]
#             if profit < 0:
#                 continue
#             else:
#                 sum += profit
#         return sum
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # k is infinite
        # dp
        # n = len(prices)
        # state = [[0, float("-inf")]] * (n+1)
        # for i, price in enumerate(prices):
        #     state[i+1][0] = max(state[i][0], state[i][1] + price)
        #     state[i+1][1] = max(state[i][1], state[i][0] - price)
        # return state[n][0]

        T_none = 0
        T_have = -prices[0]
        for price in prices[1: ]:
            T_none = max(T_none, T_have + price)
            T_have = max(T_have, T_none - price)
        return T_none