class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for index in range(1, len(prices)):
            if prices[index] > prices[index - 1]:
                profit += prices[index] - prices[index - 1]
        return profit
            