from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        res = 0
        flag = False
        for k, v in d.items():
            if v % 2 == 0:        
                res += v
            elif not flag:
                res += v
                flag = True
            else:
                res += v - 1
        return res

