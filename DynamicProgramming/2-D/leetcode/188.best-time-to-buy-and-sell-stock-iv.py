#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (38.41%)
# Total Accepted:    355.8K
# Total Submissions: 910K
# Testcase Example:  '2\n[2,4,1]'
#
# You are given an integer array prices where prices[i] is the price of a given
# stock on the i^th day, and an integer k.
# 
# Find the maximum profit you can achieve. You may complete at most k
# transactions: i.e. you may buy at most k times and sell at most k times.
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
# 
# 
# Example 1:
# 
# 
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
# 4-2 = 2.
# 
# 
# Example 2:
# 
# 
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
# 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit
# = 3-0 = 3.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000
# 
# 
#
class Solution(object):
    def maxProfit(self, k, prices):
        mem = {}
        def generateMaxProfit(index, tcount, holdingStockIndex):
            if(index == len(prices) and tcount <= k):
                return 0
            if(tcount > k or index == len(prices)):
                return -1
            if((index, tcount, holdingStockIndex) in mem):
                return mem[(index, tcount, holdingStockIndex)]
            maxProfit = 0
            if(holdingStockIndex == -1):
                maxProfit = -prices[index] + generateMaxProfit(index + 1, tcount + 1, index)
            elif(prices[holdingStockIndex] < prices[index]):
                maxProfit = prices[index] + generateMaxProfit(index + 1, tcount, -1)
            mem[(index, tcount, holdingStockIndex)] = max(maxProfit, generateMaxProfit(index + 1, tcount, holdingStockIndex))
            return mem[(index, tcount, holdingStockIndex)]
        result = generateMaxProfit(0, 0, -1)
        return result if(result >= 0) else 0
    
    def maxProfit(self, transactions, prices):
        dp = [[0] * (len(prices)) for _ in range(transactions + 1)]
        for i in range(1, transactions + 1):
            for j in range(1, len(prices)):
                dp[i][j] = dp[i][j - 1]
                for k in range(j - 1,- 1, -1):
                    if(prices[k] <= prices[j]):
                        dp[i][j] = max(dp[i][j], prices[j] - prices[k] + dp[i - 1][k])
        return dp[transactions][len(prices) - 1]


                
