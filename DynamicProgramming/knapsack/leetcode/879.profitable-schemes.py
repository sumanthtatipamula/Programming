#
# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#
# https://leetcode.com/problems/profitable-schemes/description/
#
# algorithms
# Hard (40.63%)
# Total Accepted:    55.9K
# Total Submissions: 112.9K
# Testcase Example:  '5\n3\n[2,2]\n[2,3]'
#
# There is a group of n members, and a list of various crimes they could
# commit. The i^th crime generates a profit[i] and requires group[i] members to
# participate in it. If a member participates in one crime, that member can't
# participate in another crime.
# 
# Let's call a profitable scheme any subset of these crimes that generates at
# least minProfit profit, and the total number of members participating in that
# subset of crimes is at most n.
# 
# Return the number of schemes that can be chosen. Since the answer may be very
# large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# Output: 2
# Explanation: To make a profit of at least 3, the group could either commit
# crimes 0 and 1, or just crime 1.
# In total, there are 2 schemes.
# 
# Example 2:
# 
# 
# Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# Output: 7
# Explanation: To make a profit of at least 5, the group could commit any
# crimes, as long as they commit one.
# There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and
# (0,1,2).
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 100
# 0 <= minProfit <= 100
# 1 <= group.length <= 100
# 1 <= group[i] <= 100
# profit.length == group.length
# 0 <= profit[i] <= 100
# 
# 
#
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profits: List[int]) -> int:
        mem = {}
        def traverse(index, members, profit):
            count = 0
            if(members <= n and profit >= minProfit):
                count = 1
            if(members > n or index  == len(group)):
                return count
            if((index, members, profit) in mem):
                return mem[(index, members, profit)]
            mem[(index, members, profit)] = traverse(index + 1, members + group[index], profit + profits[index]) + traverse(index + 1, members, profit)
            return mem[(index, members, profit)]
        return traverse(0,0,0)
    
     def profitableSchemes(self, n: int, minProfit: int, group: List[int], profits: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(len(group) + 1)]
        dp[0][0][0] = 1
        for i in range(1, len(group) + 1):
            for j in range(0, n + 1):
                for k in range(0, minProfit + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if(j >= group[i - 1]):
                        dp[i][j][k] += dp[i - 1][j - group[i - 1]][max(0,k - profits[i - 1])]
                        dp[i][j][k] %= mod 
        result = 0
        for i in range(0, n + 1):
            result = (result + dp[len(group)][i][minProfit]) % mod
        return result


            
        
