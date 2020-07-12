# 122. Best Time to Buy and Sell Stock II

'''
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        profit = 0
        tail = 0
        head = tail + 1
        while head < len(prices) and prices[head] < prices[tail]:
            tail += 1
            head += 1
        while head < len(prices) - 1:
            # print(tail, head)
            if prices[head + 1] < prices[head]:
                # print("next one is lesser, sell if you got sth!")
                if prices[tail] < prices[head]:
                    # print("selling")
                    profit += prices[head] - prices[tail]
                    head += 2
                    tail = head - 1
                else:
                    # print("got nothing")
                    tail = head
                    head = tail + 1
            else:
                if prices[tail] < prices[head]:
                    # print("just go on, not falling")
                    head += 1
                else:
                    # print("shift tail too")
                    tail = head
                    head = tail + 1
        # print(tail, head)
        if head < len(prices) and prices[tail] < prices[head]:
            # print("selling")
            profit += prices[head] - prices[tail]
        return profit
