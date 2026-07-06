"""You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        profit = 0
        for price in prices:
            if price < min: # Keep track of the global minimum
                min = price
            elif price - min > profit: # If the current price is greater than the minimum seen so far, if the difference is greater than maximum profit seen so far, this is max profit
                profit = price - min
        return profit
        