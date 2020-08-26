#   Minimum Cost For Tickets

'''
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.
'''


class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        last = max(days)
        days = set(days)
        dp = [0 for _ in range(last)]
        dp[-1] = min(cost)
        for i in range(last - 1, -1, -1):
            if (i + 1) in days:
                if i < last - 30:
                    dp[i] = min(dp[i + 1] + cost[0], dp[i + 7] + cost[1], dp[i + 30] + cost[2])
                elif i < last - 7:
                    dp[i] = min(dp[i + 1] + cost[0], dp[i + 7] + cost[1], cost[2])
                elif i < last - 1:
                    dp[i] = min(dp[i + 1] + cost[0], cost[1], cost[2])
            else:
                dp[i] = dp[i + 1]
        return dp[0]
