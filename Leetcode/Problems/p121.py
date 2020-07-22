# 121. Best Time to Buy and Sell Stock

'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        running_min = float("inf")
        dp = []  # what if I sold today?
        for cost in prices:
            profit = cost - running_min
            dp.append(profit)
            if cost < running_min:
                running_min = cost
        return max(max(dp), 0)
