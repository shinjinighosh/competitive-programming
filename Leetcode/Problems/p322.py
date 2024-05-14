class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)

        def util(coins, amount, dp):
            # base case
            if amount == 0:
                return 0

            if dp[amount] != -1:
                return dp[amount]

            res = float("inf")
            for coin in coins:
                if coin <= amount: # can't overshoot amount
                    res = min(res, 1 + util(coins, amount - coin, dp))
            
            dp[amount] = res
            return res
        
        result = util(coins, amount, dp) 
        if result == float("inf"):
            return -1
        return result
        
