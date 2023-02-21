#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#
# https://leetcode.com/problems/as-far-from-land-as-possible/description/
#
# algorithms
# Medium (48.49%)
# Total Accepted:    133.8K
# Total Submissions: 257.8K
# Testcase Example:  '[[1,0,1],[0,0,0],[1,0,1]]'
#
# Given an n x n grid containing only values 0 and 1, where 0 represents water
# and 1 represents land, find a water cell such that its distance to the
# nearest land cell is maximized, and return the distance. If no land or water
# exists in the grid, return -1.
# 
# The distance used in this problem is the Manhattan distance: the distance
# between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with
# distance 2.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: The cell (2, 2) is as far as possible from all the land with
# distance 4.
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
# 
# 
#
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        queue = deque([(i, j) for i in range(r) for j in range(c) if(grid[i][j] == 1)])
        if(len(queue) == r * c):
            return -1
        level = 0
        while(queue):
            for _ in range(len(queue)):
                (x, y) = queue.popleft()
                for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_x, new_y = x + i, y + j
                    if(new_x < 0 or new_y < 0 or new_x == r or new_y == c or grid[new_x][new_y] == 1):
                        continue
                    grid[new_x][new_y] = 1
                    queue.append((new_x, new_y))
            level += 1
        return level - 1
                
        
        
