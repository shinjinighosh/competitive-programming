class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1) # can we segment it upto this point?
        dp[0] = True

        for idx in range(1, len(s) + 1):
            for j in range(idx):
                if dp[j] and s[j:idx] in words:
                    dp[idx] = True
                    break

        return dp[len(s)]




