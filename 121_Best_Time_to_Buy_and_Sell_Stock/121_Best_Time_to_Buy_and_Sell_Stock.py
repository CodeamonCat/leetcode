__author__ = "CodeamonCat"
__email__ = "CodeamonCat@gmail.com"


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = 0, 0
        for idx, val in enumerate(prices):
            if val - prices[buy] > profit:
                profit = val - prices[buy]
            if prices[buy] > val:
                buy = idx
        return profit
