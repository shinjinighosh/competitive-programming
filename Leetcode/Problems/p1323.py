# 1323. Maximum 69 Number

'''
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
'''


class Solution:
    def maximum69Number(self, num: int) -> int:
        # optimum should be changing the first 6 to 9
        temp = list(str(num))
        for i, digit in enumerate(temp):
            if digit == '6':
                temp[i] = '9'
                break
        return int(''.join(temp))
