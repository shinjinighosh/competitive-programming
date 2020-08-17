# 5490. Minimum Number of Days to Eat N Oranges

'''
There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges.
You can only choose one of the actions per day.

Return the minimum number of days to eat n oranges.
'''

# TO CORRECT


class Solution:
    def minDays(self, n: int) -> int:
        res = 0
        res += n % 3
        n -= res
        while n:
            if n % 3 == 0:
                eat = 2 * n // 3
                n -= eat
                res += 1
            else:
                eat = n % 3
                n -= eat
                res += eat
        return res
