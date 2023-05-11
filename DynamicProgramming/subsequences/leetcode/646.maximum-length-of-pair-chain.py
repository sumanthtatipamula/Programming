#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
#
# algorithms
# Medium (56.50%)
# Total Accepted:    134.7K
# Total Submissions: 238.3K
# Testcase Example:  '[[1,2],[2,3],[3,4]]'
#
# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and
# lefti < righti.
# 
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can
# be formed in this fashion.
# 
# Return the length longest chain which can be formed.
# 
# You do not need to use up all the given intervals. You can select pairs in
# any order.
# 
# 
# Example 1:
# 
# 
# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
# 
# 
# Example 2:
# 
# 
# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
# 
# 
# 
# Constraints:
# 
# 
# n == pairs.length
# 1 <= n <= 1000
# -1000 <= lefti < righti <= 1000
# 
# 
#
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key =  lambda x: x[0])
        dp = [1] * (len(pairs))
        for i in range(len(pairs)):
            for j in range(i - 1, -1, -1):
                if(pairs[i][0] > pairs[j][1]):
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

    def findLongestChain(self, pairs):
        cur, res = float('-inf'), 0
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]: cur, res = p[1], res + 1
        return res
