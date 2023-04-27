#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (38.68%)
# Total Accepted:    757.5K
# Total Submissions: 2M
# Testcase Example:  '[1,2,5]\n11'
#
# <p>You are given an integer array <code>coins</code> representing coins of
# different denominations and an integer <code>amount</code> representing a
# total amount of money.</p>
# 
# <p>Return <em>the fewest number of coins that you need to make up that
# amount</em>. If that amount of money cannot be made up by any combination of
# the coins, return <code>-1</code>.</p>
# 
# <p>You may assume that you have an infinite number of each kind of coin.</p>
# 
# <p>&nbsp;</p>
# <p><strong>Example 1:</strong></p>
# 
# <pre>
# <strong>Input:</strong> coins = [1,2,5], amount = 11
# <strong>Output:</strong> 3
# <strong>Explanation:</strong> 11 = 5 + 5 + 1
# </pre>
# 
# <p><strong>Example 2:</strong></p>
# 
# <pre>
# <strong>Input:</strong> coins = [2], amount = 3
# <strong>Output:</strong> -1
# </pre>
# 
# <p><strong>Example 3:</strong></p>
# 
# <pre>
# <strong>Input:</strong> coins = [1], amount = 0
# <strong>Output:</strong> 0
# </pre>
# 
# <p><strong>Example 4:</strong></p>
# 
# <pre>
# <strong>Input:</strong> coins = [1], amount = 1
# <strong>Output:</strong> 1
# </pre>
# 
# <p><strong>Example 5:</strong></p>
# 
# <pre>
# <strong>Input:</strong> coins = [1], amount = 2
# <strong>Output:</strong> 2
# </pre>
# 
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# 
# <ul>
# <li><code>1 &lt;= coins.length &lt;= 12</code></li>
# <li><code>1 &lt;= coins[i] &lt;= 2<sup>31</sup> - 1</code></li>
# <li><code>0 &lt;= amount &lt;= 10<sup>4</sup></code></li>
# </ul>
# 
#
class Solution(object):
    def coinChange(self, coins, total):
        mem = {}
        def leastCoins(index, amount):
            if(amount == 0):
                return 0
            if(amount < 0 or index == len(coins)):
                return total + 1
            if((index, amount) in mem):
                return mem[(index, amount)] 
            mem[(index, amount)] = min(1 + leastCoins(index, amount - coins[index]), leastCoins(index + 1, amount))
            return mem[(index, amount)]
        result = leastCoins(0, total)
        return result if(result <= total) else -1
    
    def coinChange(self, coins, total):
        dp = [[float("Inf") for j in range(total + 1)] for i in range(len(coins) + 1)]
        dp[0][0] = 0
        for i in range(1, len(coins) + 1):
            for j in range(0, total + 1):
                dp[i][j] = dp[i -  1][j]
                if(j >= coins[i - 1] and dp[i][j - coins[i - 1]] != float("Inf")):
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)
        # print(dp)
        return dp[len(coins)][total] if(dp[len(coins)][total] != float("Inf")) else -1
    
    def coinChange(self, coins, total):
        dp = [float("Inf") for j in range(total + 1)]
        dp[0] = 0
        for i in range(1, len(coins) + 1):
            for j in range(coins[i - 1], total + 1):
                if(dp[j - coins[i - 1]] != float("Inf")):
                    dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)
        return dp[total] if(dp[total] != float("Inf")) else -1

        
