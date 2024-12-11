class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        DP solution 
        Time- complexity: O(n*M)
        space complexity: O(n)
        """
        #dp[i] is the minimum numbers of coins needed to make up to amount i.
        dp = [amount+1] * (amount + 1)
        dp[0] = 0 #base case (0 coins needed to make 0)

        #calculate minimum coins required for each amount a from 1 to amount
        for a in range(1,amount + 1):
            for c in coins: # iterate over coins available
                """
                Logic:
                If it's possible to use the current coin c (i.e., a - c >= 0), then:
                Consider using this coin, which adds 1 coin to the number of coins needed for a - c (stored in dp[a - c]).
                Update dp[a] to the minimum value between its current value and 1 + dp[a - c].
                """
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+ dp[a - c])
        
        #so the additional index added in dp represents infinity which is no combinations
        return dp[amount] if dp[amount] != amount + 1 else -1


        

        