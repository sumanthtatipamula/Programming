#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#
# https://leetcode.com/problems/number-of-enclaves/description/
#
# algorithms
# Medium (65.24%)
# Total Accepted:    93.1K
# Total Submissions: 142.4K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# You are given an m x n binary matrix grid, where 0 represents a sea cell and
# 1 represents a land cell.
# 
# A move consists of walking from one land cell to another adjacent
# (4-directionally) land cell or walking off the boundary of the grid.
# 
# Return the number of land cells in grid for which we cannot walk off the
# boundary of the grid in any number of moves.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is
# not enclosed because its on the boundary.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.
# 
# 
#
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if(i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 2):
                return [False, 0]
            if(grid[i][j] == 0):
                return [True, 0]
            grid[i][j], count = 0, 1
            for k in range(-1, 2, 2):
                row = dfs(i + k, j)
                col = dfs(i , j + k)
                if(not row[0] or not col[0]):
                    grid[i][j] = 2
                    return [False, 0]
                count += row[1] + col[1]
            return [True, count] 
        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if(grid[i][j] == 1):
                    count += dfs(i, j)[1]
        return count

        
