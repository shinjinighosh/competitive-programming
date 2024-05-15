from math import floor
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # it depends on the number of powers of 5 (that's the limiting agent)

        # def fact(n, memo={}):
        #     if n in [0, 1] and n not in memo:
        #         memo[n] = 1
        #         return memo[n]
        #     else:
        #         if n in memo:
        #             return memo[n]
        #         else:
        #             subproblem = fact(n-1, memo)
        #             memo[n] = n * subproblem
        #             return memo[n]

        # factorial = fact(n)
        # print(f"Factorial of {n} is {factorial}")

        res = 0
        curr = 5
        while curr <= n:
            res += floor(n / curr)
            curr *= 5
        return res
        
