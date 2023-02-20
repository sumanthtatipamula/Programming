#
# @lc app=leetcode id=1730 lang=python3
#
# [1730] Shortest Path to Get Food
#
# https://leetcode.com/problems/shortest-path-to-get-food/description/
#
# algorithms
# Medium (54.11%)
# Total Accepted:    52.1K
# Total Submissions: 96.2K
# Testcase Example:  '[["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]'
#
# You are starving and you want to eat food as quickly as possible. You want to
# find the shortest path to arrive at any food cell.
# 
# You are given an m x n character matrix, grid, of these different types of
# cells:
# 
# 
# '*' is your location. There is exactly one '*' cell.
# '#' is a food cell. There may be multiple food cells.
# 'O' is free space, and you can travel through these cells.
# 'X' is an obstacle, and you cannot travel through these cells.
# 
# 
# You can travel to any adjacent cell north, east, south, or west of your
# current location if there is not an obstacle.
# 
# Return the length of the shortest path for you to reach any food cell. If
# there is no path for you to reach food, return -1.
# 
# 
# Example 1:
# 
# 
# Input: grid =
# [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
# Output: 3
# Explanation: It takes 3 steps to reach the food.
# 
# 
# Example 2:
# 
# 
# Input: grid =
# [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
# Output: -1
# Explanation: It is not possible to reach the food.
# 
# 
# Example 3:
# 
# 
# Input: grid =
# [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
# Output: 6
# Explanation: There can be multiple food cells. It only takes 6 steps to reach
# the bottom food.
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[row][col] is '*', 'X', 'O', or '#'.
# The grid contains exactly one '*'.
# 
# 
#
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        r,c, queue, directions  = len(grid), len(grid[0]), deque(),  [
         (-1, 0), (0, -1), (0, 1), (1, 0)]
        for l in range(0, r):
            for m in range(0, c):
                if(grid[l][m] == '*'):
                    queue.append([l, m, 0])
                    grid[l][m] = 'X'
                    while(queue):
                        x,y,count = queue.popleft()
                        if(grid[x][y] == '#'):
                            return count
                        for i, j in directions:
                            new_x  = x + i
                            new_y  = y + j
                            if(new_x < 0 or new_y < 0 or new_x == r or new_y == c or grid[new_x][new_y] == 'X'):
                                continue
                            grid[new_x][new_y] = 'X' if(grid[new_x][new_y] != '#') else grid[new_x][new_y]
                            queue.append([new_x, new_y, count + 1])
                    return -1
        
