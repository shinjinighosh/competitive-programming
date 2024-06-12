class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] represents if s[i:j+1] is a palindrome

        n = len(s)
        if n < 2:
            return s
        dp = [[False for i in range(n)] for j in range(n)]
        start = 0
        max_length = 1

        # single letters
        for i in range(n):
            dp[i][i] = True

        # double letters
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_length = 2

        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start, max_length = i, length

        return s[start: start + max_length]
