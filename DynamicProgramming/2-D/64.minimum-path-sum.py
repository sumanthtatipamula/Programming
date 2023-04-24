#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (60.86%)
# Total Accepted:    861.1K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100
# 
# 
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c, mem = len(grid), len(grid[0]), {}
        def recursive(i, j):
            if(i < 0 or j < 0 or i == r or j == c):
                return float("Inf")
            if((i, j) in mem):
                return mem[(i, j)]
            if(i == r - 1 and j == c - 1):
                return grid[i][j]
            mem[(i,j)] = grid[i][j] + min(recursive(i + 1, j), recursive(i, j + 1))
            return mem[(i, j)]
        
        for i in range(1, r):
            grid[i][0] += grid[i -  1][0]
        for j in range(1, c):
            grid[0][j] += grid[0][j - 1]
        
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[r - 1][c - 1]
        
        
