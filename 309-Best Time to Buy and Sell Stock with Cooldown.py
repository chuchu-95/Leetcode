class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cooldown i-2
        T_none = 0
        T_have = float("-inf")
        T_none_pre = 0
        for i, price in enumerate(prices):
            temp  = T_none
            T_none = max(T_none, T_have + price)
            T_have = max(T_have, T_none_pre - price)
            T_none_pre = temp
        return T_none