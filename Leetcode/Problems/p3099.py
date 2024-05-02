class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_digits = 0
        for i in str(x):
            sum_digits += int(i)
        return sum_digits if x % sum_digits == 0 else -1
