#   Reverse Bits

'''
Reverse bits of a given 32 bits unsigned integer.
'''


class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n).replace("0b", "")
        n = "0" * (32 - len(n)) + n
        return int(n[::-1], 2)
