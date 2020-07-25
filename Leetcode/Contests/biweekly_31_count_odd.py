# 5456. Count Odd Numbers in an Interval Range

'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
'''


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # count = 0
        # for i in range(low, high+1):
        # if i%2:
        # count +=1
        if low % 2 == 0 and high % 2 == 0:  # 10, 16 -> 3
            return (high - low) // 2
        elif low % 2 == 0 and high % 2 == 1:  # 10, 15 -> 3
            return (high + 1 - low) // 2
        elif low % 2 == 1 and high % 2 == 0:  # 9, 12 -> 2
            return (high - low) // 2 + 1
        else:  # 9, 15 -> 4
            return (high - low) // 2 + 1
        # return count
