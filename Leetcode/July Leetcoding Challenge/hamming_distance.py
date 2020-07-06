#   Hamming Distance

'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = bin(x)
        y_bin = bin(y)
        if len(x_bin) > len(y_bin):
            padding = "0" * (len(x_bin) - len(y_bin))
            x_bin = x_bin[2:]
            y_bin = padding + y_bin[2:]
        elif len(y_bin) > len(x_bin):
            padding = "0" * (len(y_bin) - len(x_bin))
            y_bin = y_bin[2:]
            x_bin = padding + x_bin[2:]
        else:
            x_bin = x_bin[2:]
            y_bin = y_bin[2:]
        ctr = 0
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                ctr += 1
        return ctr
