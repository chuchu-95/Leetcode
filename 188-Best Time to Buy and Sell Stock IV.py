class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # standard dp condition
        # n = len(prices)
        # state = [[[0, float("-inf")] for _ in range(k+1)] for _ in range(n+1)]
        # for i, price in enumerate(prices):
        #     for k in range(1, k+1):
        #         state[i+1][k][0] = max(state[i][k][0], state[i][k][1] + price)
        #         state[i+1][k][1] = max(state[i][k][1], state[i][k-1][0] - price)
        # return state[n][k][0]

        n = len(prices)
        if k > n//2:
            #greedy
            resMax = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    resMax += (prices[i] - prices[i-1])
            return resMax
        T_none = [0 for _ in range(k+1)]
        T_have = [float("-inf") for _ in range(k+1)]
        for price in prices:
            for i in range(k, 0, -1):
                T_none[i] = max(T_none[i], T_have[i] + price)
                T_have[i] = max(T_have[i], T_none[i-1] - price)
        return T_none[k]
