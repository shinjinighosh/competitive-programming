#   Permutation Sequence


'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
'''


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = list(range(1, n + 1))
        res = ""

        for i in range(n):
            d = (k - 1) // factorial(n - 1)
            k -= d * factorial(n - 1)
            n -= 1
            res += str(num[d])
            num.pop(d)

        return res
