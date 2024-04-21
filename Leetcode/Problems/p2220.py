class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        start_bin = str(bin(start)[2:])
        end_bin = str(bin(goal)[2:])

        if len(start_bin) < len(end_bin):
            start_bin = "0" * (len(end_bin) - len(start_bin)) + start_bin
        elif len(end_bin) < len(start_bin):
            end_bin = "0" * (len(start_bin) - len(end_bin)) + end_bin

        ctr = 0
        for i, j in zip(start_bin, end_bin):
            if i != j:
                ctr += 1
        return ctr
