# 1281. Subtract the Product and Sum of Digits of an Integer

'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = map(int, str(n))
        prod = 1
        s = 0
        for digit in digits:
            prod *= digit
            s += digit
        return prod - s
