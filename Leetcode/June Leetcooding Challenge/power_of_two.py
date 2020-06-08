import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # eps = 0.000000001
        # l = math.log(n, 2)
        # return abs(round(l) - l) < eps
        if n == 1:
            return True
        if n < 1:
            return False
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                return False
        return True


testcase = Solution()
testcases = [2147483647, 536870912, 268435455, 2097151, 1, 2, 4, 8, 18]
expected = [False, True, False, False, True, True, True, True, False]
for i, num in enumerate(testcases):
    if testcase.isPowerOfTwo(num) != expected[i]:
        print(f"for {num} expected {expected[i]} got reverse")
