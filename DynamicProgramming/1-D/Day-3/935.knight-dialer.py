#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#
# https://leetcode.com/problems/knight-dialer/description/
#
# algorithms
# Medium (50.17%)
# Total Accepted:    98.3K
# Total Submissions: 194.9K
# Testcase Example:  '1'
#
# The chess knight has a unique movement, it may move two squares vertically
# and one square horizontally, or two squares horizontally and one square
# vertically (with both forming the shape of an L). The possible movements of
# chess knight are shown in this diagaram:
# 
# A chess knight can move as indicated in the chess diagram below:
# 
# We have a chess knight and a phone pad as shown below, the knight can only
# stand on a numeric cell (i.e. blue cell).
# 
# Given an integer n, return how many distinct phone numbers of length n we can
# dial.
# 
# You are allowed to place the knight on any numeric cell initially and then
# you should perform n - 1 jumps to dial a number of length n. All jumps should
# be valid knight jumps.
# 
# As the answer may be very large, return the answer modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 10
# Explanation: We need to dial a number of length 1, so placing the knight over
# any numeric cell of the 10 cells is sufficient.
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 20
# Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29,
# 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
# 
# 
# Example 3:
# 
# 
# Input: n = 3131
# Output: 136006598
# Explanation: Please take care of the mod.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 5000
# 
# 
#
class Solution:
    def knightDialer(self, n: int) -> int:
        r, c, mod = 4, 3, (10 ** 9) + 7
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        mem = {}
        dp = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(n + 1)]
        def traverse(i, j, length):
            if(i < 0 or j < 0 or i >= r or j >= c or (i == 3 and (j != 1))):
                return 0
            if(length == 1):
                return 1
            if(dp[length][i][j] > 0):
                return dp[length][i][j]
            count = 0
            for x, y in directions:
                new_x, new_y = x + i, y + j
                count += traverse(new_x, new_y, length - 1) % mod
                count %=  mod
            dp[length][i][j] = count
            return count
        result = 0
        for i in range(4):
            for j in range(3):
                result += traverse(i, j, n) % mod
                result %= mod
        return result
        
