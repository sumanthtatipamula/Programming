#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
#
# algorithms
# Medium (44.56%)
# Total Accepted:    291K
# Total Submissions: 652.4K
# Testcase Example:  '[[0,1],[1,0]]'
#
# Given an n x n binary matrix grid, return the length of the shortest clear
# path in the matrix. If there is no clear path, return -1.
# 
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0,
# 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
# 
# 
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they
# are different and they share an edge or a corner).
# 
# 
# The length of a clear path is the number of visited cells of this path.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,1],[1,0]]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
# 
# 
#
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        r,c, result, queue, directions  = len(grid), len(grid[0]), 0, deque(),  [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        if(grid[0][0] == 1 or grid[r - 1][c- 1] == 1):
            return -1
        queue.append([0,0, 1])
        grid[0][0] = 1
        while(queue):
            x,y,count = queue.popleft()
            if(x ==  (r - 1) and y == (c - 1)):
                return count
            for i, j in directions:
                new_x  = x + i
                new_y  = y + j
                if(new_x < 0 or new_y < 0 or new_x == r or new_y == c or grid[new_x][new_y] == 1):
                    continue
                grid[new_x][new_y] = 1
                queue.append([new_x, new_y, count + 1])
        return -1
