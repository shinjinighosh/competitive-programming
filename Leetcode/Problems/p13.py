# 13. Roman to Integer

'''
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

'''


class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        idx = 0
        res = 0
        l = len(s)
        while idx < l:
            if idx + 1 < l:
                this = s[idx]
                n = s[idx + 1]
                if (this == 'I' and n in ['V', 'X']) or (this == 'X' and n in ['L', 'C']) or (this == 'C' and n in ['D', 'M']):
                    res += mapping[n] - mapping[this]
                    idx += 2
                    continue
                else:
                    res += mapping[this]
                    idx += 1
                    continue
            else:
                res += mapping[s[idx]]
                idx += 1
        return res
