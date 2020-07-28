# 728. Self Dividing Numbers

'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
'''


class Solution:
    def selfDiv(self, num):
        digits = map(int, str(num))
        for i in digits:
            if not i or num % i != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        counter = left
        res = []
        while counter <= right:
            if self.selfDiv(counter):
                res.append(counter)
            counter += 1
        return res
