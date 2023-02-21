#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#
# https://leetcode.com/problems/shortest-bridge/description/
#
# algorithms
# Medium (54.19%)
# Total Accepted:    122.8K
# Total Submissions: 226.2K
# Testcase Example:  '[[0,1],[1,0]]'
#
# You are given an n x n binary matrix grid where 1 represents land and 0
# represents water.
# 
# An island is a 4-directionally connected group of 1's not connected to any
# other 1's. There are exactly two islands in grid.
# 
# You may change 0's to 1's to connect the two islands to form one island.
# 
# Return the smallest number of 0's you must flip to connect the two
# islands.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,1],[1,0]]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.
# There are exactly two islands in grid.
# 
# 
#
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        r , c, queue  = len(grid), len(grid[0]), deque()
        def dfs(i, j):
            if(i < 0 or j < 0 or i == r or j == c or grid[i][j] == 2 or grid[i][j] == 0):
                return
            queue.append((i,j))
            grid[i][j] = 2
            for k in range(-1, 2, 2):
                dfs(i + k, j)
                dfs(i, j + k)

        for i in range(r):
            for j in range(c):
                if(grid[i][j] == 1):
                    dfs(i, j)
                    level = 0
                    while(queue):
                        for _ in range(len(queue)):
                            x, y = queue.popleft()
                            for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                                    new_x, new_y = x + i, y + j
                                    if(new_x < 0 or new_y < 0 or new_x == r or new_y == c or grid[new_x][new_y] == 2):
                                        continue
                                    if(grid[new_x][new_y] == 1):
                                        return level
                                    grid[new_x][new_y] = 2
                                    queue.append((new_x, new_y))
                        level += 1
        return - 1

        
