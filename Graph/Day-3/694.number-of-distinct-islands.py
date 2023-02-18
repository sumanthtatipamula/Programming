#
# @lc app=leetcode id=694 lang=python3
#
# [694] Number of Distinct Islands
#
# https://leetcode.com/problems/number-of-distinct-islands/description/
#
# algorithms
# Medium (60.69%)
# Total Accepted:    145.9K
# Total Submissions: 240.3K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
# 
# An island is considered to be the same as another if and only if one island
# can be translated (and not rotated or reflected) to equal the other.
# 
# Return the number of distinct islands.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.
# 
# 
#
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        serialset = set()
        def dfs(i, j):
            if(i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0):
                return ""
            grid[i][j] = 0
            return "U" + dfs(i + 1, j) + ",D" + dfs(i - 1 , j) + ",L" + dfs(i, j- 1) + ',R' + dfs(i , j + 1)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if(grid[i][j] == 1):
                    serialset.add(dfs(i,j))
        return len(serialset)

        
