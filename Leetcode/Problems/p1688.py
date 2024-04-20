class Solution:
    def numberOfMatches(self, n: int) -> int:
        num_matches = 0
        if n == 1:
            return num_matches
        while n != 1:
            if n % 2 == 0:
                num_matches += int(n/2)
                n /= 2
            else:
                num_matches += int((n-1)/2)
                n = (n-1) / 2 + 1
        return num_matches

