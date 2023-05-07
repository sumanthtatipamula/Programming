#
# @lc app=leetcode id=1866 lang=python3
#
# [1866] Number of Ways to Rearrange Sticks With K Sticks Visible
#
# https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/description/
#
# algorithms
# Hard (55.58%)
# Total Accepted:    11.1K
# Total Submissions: 19.8K
# Testcase Example:  '3\n2'
#
# There are n uniquely-sized sticks whose lengths are integers from 1 to n. You
# want to arrange the sticks such that exactly k sticks are visible from the
# left. A stick is visible from the left if there are no longer sticks to the
# left of it.
# 
# 
# For example, if the sticks are arranged [1,3,2,5,4], then the sticks with
# lengths 1, 3, and 5 are visible from the left.
# 
# 
# Given n and k, return the number of such arrangements. Since the answer may
# be large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 2
# Output: 3
# Explanation: [1,3,2], [2,3,1], and [2,1,3] are the only arrangements such
# that exactly 2 sticks are visible.
# The visible sticks are underlined.
# 
# 
# Example 2:
# 
# 
# Input: n = 5, k = 5
# Output: 1
# Explanation: [1,2,3,4,5] is the only arrangement such that all 5 sticks are
# visible.
# The visible sticks are underlined.
# 
# 
# Example 3:
# 
# 
# Input: n = 20, k = 11
# Output: 647427950
# Explanation: There are 647427950 (mod 10^9 + 7) ways to rearrange the sticks
# such that exactly 11 sticks are visible.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 1 <= k <= n
# 
# 
#
from functools import lru_cache
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        used = [False] * (n + 1)
        @lru_cache(maxsize = None)
        def find_ways(sticksLeft, max_left, visibleSticksCount):
            if(sticksLeft == 0 and visibleSticksCount == k):
                return 1
            if(sticksLeft == 0):
                return 0
            ways = 0
            for i in range(1, n + 1):
                if(used[i]):
                    continue;
                used[i] = True
                ways = (ways + find_ways(sticksLeft - 1, max(max_left, i), visibleSticksCount + 1 if(i > max_left) else visibleSticksCount)) % mod
                used[i] = False
            return ways
        return find_ways(n, 0, 0)
    
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                dp[i][j] = ((i - 1) * dp[i - 1][j] + dp[i - 1][j - 1]) % mod
        return dp[n][k]
