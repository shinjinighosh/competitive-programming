class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [] # profit if I sold today after buying at min possible time so far
        curr_min = float("inf")
        for idx, price in enumerate(prices):
            dp.append(price - curr_min)
            if price < curr_min:
                curr_min = price
        return max(max(dp), 0)
