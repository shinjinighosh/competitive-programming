# 1492. The kth Factor of n

'''
Given two positive integers n and k.

A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
'''


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        counter = 0
        for i in range(1, n + 1):
            if n % i == 0:
                counter += 1
                if counter == k:
                    return i
        return -1
