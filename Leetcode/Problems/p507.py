# 507. Perfect Number

'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
'''


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 0
        if num <= 1:
            return False
        sqrt = int(num ** 0.5)
        for i in range(1, sqrt + 1):
            if num % i == 0:
                s += i
                if num != i * i and i != 1:
                    s += num // i
            # print(i, s)
            if s > num:
                return False
        return s == num
