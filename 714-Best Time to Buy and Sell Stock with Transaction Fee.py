class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # fee (add when buy or sell) infinite times
        T_none = 0
        T_have = float("-inf")
        for i, price in enumerate(prices):
            temp = T_none
            T_none = max(T_none, T_have + price - fee)
            T_have = max(T_have, temp - price)
        return T_none
