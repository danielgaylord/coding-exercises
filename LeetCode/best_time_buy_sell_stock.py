class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = float('inf')
        profit = 0
        for index, amount in enumerate(prices):
            sell = amount if amount < sell else sell
            profit = max(profit, amount - sell)
        return profit