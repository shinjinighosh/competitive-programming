# 1518. Water Bottles

'''
Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the maximum number of water bottles you can drink.
'''


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        current_bottles = numBottles  # empty
        total = numBottles  # total drank
        while current_bottles >= numExchange:  # enough empty to exchange
            # print(current_bottles)
            new_bottles = current_bottles // numExchange
            total += new_bottles
            current_bottles = (current_bottles % numExchange) + new_bottles
            # drank = current_bottles // numExchange
            # total += drank
            # current_bottles -= drank
        # total += current_bottles
        return total
