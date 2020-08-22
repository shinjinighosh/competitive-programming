# 5479. Thousand Separator

'''
Given an integer n, add a dot (".") as the thousands separator and return it in string format.
'''


class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = []
        if n == 0:
            return "0"
        if not n:
            return ""
        if len(str(n)) == 1:
            return str(n)
        digits = list(str(n))
        print(digits)
        counter = 1
        while counter <= len(str(n)):
            res.append(digits.pop())
            if counter % 3 == 0:
                res.append(".")
            counter += 1
        return "".join(res[::-1]).lstrip(".")
