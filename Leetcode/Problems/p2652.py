class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # number of numbers is mul(3) + mul(5) + mul(7) - mul(3, 5) - mul(5, 7) - mul(3, 7) + mul(3, 5, 7)
        # mul = lambda n, factor: int(n / factor)
        # return mul(n, 3) + mul(n, 5) + mul(n, 7) - mul(n, 15) - mul(n, 35) - mul(n, 21) + mul(n, 105)

        s = 0
        for i in range(1, n+1):
            if i%3 == 0 or i%5 == 0 or i%7 == 0:
                s += i
        return s
