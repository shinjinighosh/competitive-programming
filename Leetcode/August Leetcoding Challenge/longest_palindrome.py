# Longest Palindrome

'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.
'''

import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum([freq % 2 for _, freq in Counter(s).items()])
        return len(s) if odds <= 1 else len(s) - odds + 1

        # ans = 0
        # for v in collections.Counter(s).itervalues():
        #     ans += v / 2 * 2
        #     if ans % 2 == 0 and v % 2 == 1:
        #         ans += 1
        # return ans

        # freq = {}
        # for i in s:
        #     if s not in freq:
        #         freq[s] = 1
        #     else:
        #         freq[s] += 1
        # res = 0
        # for key, val in freq.items():
        #     res += val / 2 * 2
        #     if res % 2 == 0 and val % 2 == 1:
        #         res += 1
        # # if res < len(freq) * 2:
        #     # res += 1
        # return res
