class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return profit
        l = 0
        for idx, price in enumerate(prices):
            if price > prices[l]:
                profit = max(profit, price - prices[l])
            else:
                l = idx
        return profit      