# 91. Decode Ways

'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1 for _ in range(len(s))]
        if not s or s[0] == "0":
            return 0
        elif len(s) == 1:
            return 1 if 1 <= int(s) <= 9 else 0
        for i in range(1, len(s)):
            if 10 <= int(s[i - 1:i + 1]) <= 26 and s[i] != "0":
                dp[i] = dp[i - 1] + dp[i - 2]
            elif 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] = dp[i - 2]
            elif 1 <= int(s[i]) <= 9:
                dp[i] = dp[i - 1]
            else:
                dp[i] = 0
        # print(dp)
        return dp[-1]
