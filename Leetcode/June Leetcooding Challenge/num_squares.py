#   Perfect Squares

'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

'''


class Solution:
    def numSquares(self, n: int) -> int:
        # using Lagrange's four-square theorem
        if int(sqrt(n))**2 == n:
            return 1

        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j * j))**2 == n - j * j:
                return 2

        while n % 4 == 0:
            n >>= 2

        if n % 8 == 7:
            return 4

        return 3
