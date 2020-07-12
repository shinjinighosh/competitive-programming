# 693. Binary Number with Alternating Bits
'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

'''


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = str(bin(n))
        for i in range(len(binary) - 1):
            if binary[i] == binary[i + 1]:
                return False
        return True
