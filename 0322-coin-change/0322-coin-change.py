class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        # initializes dp = [0, ..., amount, amount + 1]

        for a in range(1, amount + 1): # start at index 1
            for coin in coins:
                if a - coin >= 0: # checks if amount - coin = negative value
                    dp[a] = min(dp[a], 1 + dp[a - coin]) # min() of dp[a] and 1 + dp[amount - coin]
        
        return dp[amount] if dp[amount] != amount + 1 else -1 