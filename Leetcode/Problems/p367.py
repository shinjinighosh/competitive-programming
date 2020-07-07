# 367. Valid Perfect Square

'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        for i in range(2, num // 2 + 1):
            if i * i == num:
                return True
            elif i * i > num:
                return False
