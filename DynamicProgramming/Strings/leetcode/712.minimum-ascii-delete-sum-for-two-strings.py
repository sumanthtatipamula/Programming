#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (62.43%)
# Total Accepted:    76.5K
# Total Submissions: 122.3K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings s1 and s2, return the lowest ASCII sum of deleted
# characters to make two strings equal.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
# 
# 
# Example 2:
# 
# 
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is
# 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers
# of 433 or 417, which are higher.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 1000
# s1 and s2 consist of lowercase English letters.
# 
# 
#
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        mem = {}
        def min_cost(index1, index2):
            if(index1 == len(s1) and index2 == len(s2)):
                return 0
            if((index1, index2) in mem):
                return mem[(index1, index2)]
            if(index1 == len(s1)):
                return sum([ord(s2[i]) for i in range(index2, len(s2))])
            if(index2 == len(s2)):
                return sum([ord(s1[i]) for i in range(index1, len(s1))])
            if(s1[index1] == s2[index2]):
                mem[(index1, index2)] = min_cost(index1 + 1, index2 + 1)
                return mem[(index1, index2)]
            mem[(index1, index2)] = min(ord(s1[index1]) + min_cost(index1 + 1, index2), ord(s2[index2]) + min_cost(index1, index2 + 1))
            return mem[(index1, index2)]
        return min_cost(0, 0)
    
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(1, len(s2) + 1):
            dp[0][i] = ord(s2[i - 1]) + dp[0][i - 1]
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if(s1[i - 1] == s2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(ord(s1[i - 1]) + dp[i - 1][j], ord(s2[j - 1]) + dp[i][j - 1])
        return dp[len(s1)][len(s2)]


