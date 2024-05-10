class Solution:
    def isHappy(self, n: int) -> bool:
        sum_digit_sq = lambda x: sum([int(i)**2 for i in str(x)])
        if n == 1:
            return True
        seen = set()
        while True:
            n = sum_digit_sq(n)
            if n == 1:
                return True
            if n in seen: # we have looped and not seen 1
                return False
            seen.add(n)
