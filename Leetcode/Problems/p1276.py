# 1276. Number of Burgers with No Waste of Ingredients

'''
Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:

Jumbo Burger: 4 tomato slices and 1 cheese slice.
Small Burger: 2 Tomato slices and 1 cheese slice.
Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].
'''


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # x Jumbo, y Small
        # check if we can make it equal to 0
        T, C = tomatoSlices, cheeseSlices  # making them easier to read
        if (T - 2 * C) % 2 == 0 and (4 * C - T) % 2 == 0 and (T - 2 * C) >= 0 and (4 * C - T) >= 0:
            return [(T - 2 * C) // 2, (4 * C - T) // 2]
        else:
            return []
