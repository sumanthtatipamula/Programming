#
# @lc app=leetcode id=1269 lang=python3
#
# [1269] Number of Ways to Stay in the Same Place After Some Steps
#
# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/description/
#
# algorithms
# Hard (43.62%)
# Total Accepted:    32.1K
# Total Submissions: 73.8K
# Testcase Example:  '3\n2'
#
# You have a pointer at index 0 in an array of size arrLen. At each step, you
# can move 1 position to the left, 1 position to the right in the array, or
# stay in the same place (The pointer should not be placed outside the array at
# any time).
# 
# Given two integers steps and arrLen, return the number of ways such that your
# pointer is still at index 0 after exactly steps steps. Since the answer may
# be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: steps = 3, arrLen = 2
# Output: 4
# Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
# Right, Left, Stay
# Stay, Right, Left
# Right, Stay, Left
# Stay, Stay, Stay
# 
# 
# Example 2:
# 
# 
# Input: steps = 2, arrLen = 4
# Output: 2
# Explanation: There are 2 differents ways to stay at index 0 after 2 steps
# Right, Left
# Stay, Stay
# 
# 
# Example 3:
# 
# 
# Input: steps = 4, arrLen = 2
# Output: 8
# 
# 
# 
# Constraints:
# 
# 
# 1 <= steps <= 500
# 1 <= arrLen <= 10^6
# 
# 
#
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        mem = {}
        def findWays(steps, index):
            if(steps == 0 and index == 0):
                return 1
            if(steps == 0 or index == arrLen):
                return 0
            if((steps, index) in mem):
                return mem[(steps, index)]
            ways = 0
            ways = findWays(steps - 1, index)
            if(index > 0):
                ways = (ways + findWays(steps - 1, index - 1)) % mod
            mem[(steps, index)] = (ways + findWays(steps - 1, index + 1)) % mod
            return mem[(steps, index)]
        return findWays(steps, 0)
    
    
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        end = min(steps // 2 + 1, arrLen)
        dp = [[0] * (end + 2) for _ in range(steps + 1)]
        dp[0][1] = 1
        for i in range(1, steps + 1):
            for j in range(1, end + 1):
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod
        return dp[steps][1]
