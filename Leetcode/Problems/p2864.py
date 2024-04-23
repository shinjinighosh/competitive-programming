class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # max odd binary number will have all the 1s up front, then 0s, then last 1
        num_ones = s.count("1")
        num_zeros = s.count("0")

        if num_ones == 1:
            return num_zeros * "0" + "1"
        else:
            return (num_ones-1) * "1" + num_zeros * "0" + "1"
        
