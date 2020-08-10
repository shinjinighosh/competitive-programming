# Excel Sheet Column Number

'''
Given a column title as appear in an Excel sheet, return its corresponding column number.
'''


class Solution:
    def titleToNumber(self, s: str) -> int:
        def getNum(letter):
            return ord(letter) - 64
        letters = list(s)
        base = 1
        res = 0
        while letters:
            l = letters.pop()
            res += base * getNum(l)
            base *= 26
        return res
