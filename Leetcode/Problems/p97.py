class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # dp[i][j] represents if it's possible to interleave s1[:i] and s2[:j] to form s3[:i+j]
        m, n = len(s1), len(s2)
        dp = [[False for _ in range(n+1)] for i in range(m+1)]

        if m + n != len(s3):
            return False

        if not m and not n:
            return not s3
        
        if m and not n:
            return s1 == s3
        elif n and not m:
            return s2 == s3

        dp[0][0] = True

        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and (s1[:i] == s3[:i])
        
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and (s2[:j] == s3[:j])

        for i in range(1, m+1):
            for j in range(1, n+1):
                if dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                    continue
                elif dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True
        
        return dp[-1][-1]
