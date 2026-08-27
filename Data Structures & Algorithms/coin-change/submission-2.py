class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # [1,5,10] -> dp[0,0,0] -> dp [11,7,2]

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1

        # memo = {}

        # def dfs(amount): 
        #     if amount == 0:
        #         return 0
            
        #     if amount in memo:
        #         return memo[amount]
            
        #     res = 1e9
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount - coin))
                
        #     memo[coin] = amount
            
        #     return res
        
        # min_coins = dfs(amount)
        # return -1 if min_coins >= 1e9 else min_coins
            
