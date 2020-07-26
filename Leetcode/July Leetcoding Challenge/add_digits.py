# Add Digits

'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
'''


class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            digits = map(int, list(str(num)))
            num = sum(digits)
        return num
