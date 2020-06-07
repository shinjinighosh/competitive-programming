# 771. Jewels and Stones


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        for char in S:
            if char in J:
                res += 1
        return res
