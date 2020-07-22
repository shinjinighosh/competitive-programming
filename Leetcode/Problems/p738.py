# 738. Monotone Increasing Digits

'''
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)
'''


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        res = []
        A = list(map(int, str(N)))
        for i in range(len(A)):
            for d in range(1, 10):
                if res + [d] * (len(A) - i) > A:
                    res.append(d - 1)
                    break
            else:
                res.append(9)

        return int("".join(map(str, res)))
