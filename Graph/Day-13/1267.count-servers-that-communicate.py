#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#
# https://leetcode.com/problems/count-servers-that-communicate/description/
#
# algorithms
# Medium (59.33%)
# Total Accepted:    50.6K
# Total Submissions: 85.1K
# Testcase Example:  '[[1,0],[0,1]]'
#
# You are given a map of a server center, represented as a m * n integer matrix
# grid, where 1 means that on that cell there is a server and 0 means that it
# is no server. Two servers are said to communicate if they are on the same row
# or on the same column.
# 
# Return the number of servers that communicate with any other server.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.
# 
# Example 2:
# 
# 
# 
# 
# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other
# server.
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each
# other. The two servers in the third column can communicate with each other.
# The server at right bottom corner can't communicate with any other
# server.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1
# 
# 
#
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        processed, result, r, c = set(), 0, len(grid), len(grid[0])
        def dfs(i, j):
            if(grid[i][j] == 0):
                return 0
            count = 1
            grid[i][j] = 0
            row_key = 'r' + str(i)
            col_key = 'c' + str(j)
            if(row_key not in processed):
                processed.add(row_key)
                for k in range(0, c):
                    if(grid[i][k] == 1):
                        count += dfs(i, k)
            if(col_key not in processed):
                processed.add(col_key)
                for k in range(0, r):
                    if(grid[k][j] == 1):
                        count += dfs(k, j)
            return count

        for i in range(r):
            for j in range(c):
                if(grid[i][j] == 1):
                    count = dfs(i, j)
                    result += count if(count > 1) else 0
        return result
        
