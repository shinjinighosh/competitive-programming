# 1137. N-th Tribonacci Number

'''
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
'''


class Solution:
    cache = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n not in Solution.cache:
            Solution.cache[n] = self.tribonacci(
                n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return Solution.cache[n]
