# Best Time to Buy and Sell Stock III

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''

# O(n) solution


class Solution:
    def maxSingle(self, prices):  # what if I had only one transaction
        if not prices:
            return 0
        min_so_far = [i for i in prices]
        _min = prices[0]
        for i in range(len(prices)):
            if prices[i] < _min:
                _min = prices[i]
            else:
                min_so_far[i] = _min
        dp = [0 for i in prices]
        for i in range(1, len(prices)):
            dp[i] = max(0, prices[i] - min_so_far[i])  # what if we sold on this day
        # print(dp)
        return dp

    def maxProfit(self, prices: List[int]) -> int:
        _max = 0
        forward_profits = self.maxSingle(prices)
        if not prices:
            return 0

        # for i in range(len(prices)):
        #     temp = self.maxSingle(prices[:i]) + self.maxSingle(prices[i:])
        #     if temp > _max:
        #         _max = temp

        max_so_far = prices[-1]
        max_profit = 0
        for i in range(len(prices) - 1, 0, -1):
            if prices[i] > max_so_far:
                max_so_far = prices[i]
            if max_so_far - prices[i] > max_profit:  # what if we bought on this day
                max_profit = max_so_far - prices[i]
            if max_profit + forward_profits[i] > _max:
                _max = max_profit + forward_profits[i]

        return _max
        # print(self.maxSingle(prices))


# O(n^2) solution
# class Solution:
#     def maxSingle(self, prices):  # what if I had only one transaction
#         if not prices:
#             return 0
#         min_so_far = [i for i in prices]
#         _min = prices[0]
#         for i in range(len(prices)):
#             if prices[i] < _min:
#                 _min = prices[i]
#             else:
#                 min_so_far[i] = _min
#         dp = [0 for i in prices]
#         for i in range(1, len(prices)):
#             dp[i] = max(0, prices[i] - min_so_far[i])
#         # print(dp)
#         return max(dp)
#
#     def maxProfit(self, prices: List[int]) -> int:
#         _max = 0
#         if not prices:
#             return 0
#         for i in range(len(prices)):
#             temp = self.maxSingle(prices[:i]) + self.maxSingle(prices[i:])
#             if temp > _max:
#                 _max = temp
#         return _max
#         # print(self.maxSingle(prices))
