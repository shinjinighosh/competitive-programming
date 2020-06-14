# 5438. Minimum Number of Days to Make m Bouquets

'''
Given an integer array bloomDay, an integer m and an integer k.

We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
'''


class Solution:
    def minDays(self, bloomDay, m, k):
        if len(bloomDay) < m * k:
            return -1
        elif len(bloomDay) == m * k:  # need all flowers
            return max(bloomDay)
        # start at day min(bloomDay)
        res = min(bloomDay)
        state_of_garden = []
        # initialize garden
        for day in bloomDay:
            if day == res:
                state_of_garden.append(1)
            else:
                state_of_garden.append(0)

        # print("initial state of garden on day", res, "is ", state_of_garden)
        max_day = max(bloomDay)
        while res <= max_day:
            if self.checkPossibility(state_of_garden, m, k):
                return res
            else:
                res += 1
                for i in range(len(bloomDay)):
                    if bloomDay[i] == res:
                        state_of_garden[i] = 1
                # print("state of garden on day ", res, "is ", state_of_garden)
        return -1

    def checkPossibility(self, garden, m, k):
        i = 0  # pointer to place in garden
        l = len(garden)
        bouquet = [1] * k
        while i <= l - k:
            if garden[i:i + k] == bouquet:
                # print("got a bouquet from i to i+k as", i, i + k)
                i += k
                m -= 1
                if m == 0:
                    return True
            else:  # move one place, can optimize to move to 1 after next 0
                i += 1
        return False


bdays = [[1, 10, 3, 10, 2], [1, 10, 3, 10, 2], [7, 7, 7, 7, 12, 7, 7],
         [1000000000, 1000000000], [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]]
ms = [3, 3, 2, 1, 4]
ks = [1, 2, 3, 1, 2]
exp = [3, -1, 12, 1000000000, 9]

testcase = Solution()
for i in range(len(ms)):
    print("answer", testcase.minDays(bdays[i], ms[i], ks[i]), "Expected ", exp[i])
