#   Numbers With Same Consecutive Differences

'''
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.
'''


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        def helper(n):
            if n == 1:
                for i in range(10):
                    yield str(i)
            else:
                for prev in helper(n - 1):
                    if 0 <= (int(prev[-1]) + K) <= 9:
                        yield prev + str(int(prev[-1]) + K)
                    if 0 <= (int(prev[-1]) - K) <= 9:
                        yield prev + str(int(prev[-1]) - K)
        return list(set([int(x) for x in helper(N) if not (x[0] == '0' and len(x) != 1)]))
