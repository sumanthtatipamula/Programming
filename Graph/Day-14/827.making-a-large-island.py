#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#
# https://leetcode.com/problems/making-a-large-island/description/
#
# algorithms
# Hard (44.79%)
# Total Accepted:    127.2K
# Total Submissions: 283.5K
# Testcase Example:  '[[1,0],[0,1]]'
#
# You are given an n x n binary matrix grid. You are allowed to change at most
# one 0 to be 1.
# 
# Return the size of the largest island in grid after applying this operation.
# 
# An island is a 4-directionally connected group of 1s.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with
# area = 3.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island
# with area = 4.
# 
# Example 3:
# 
# 
# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.
# 
#
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        distinctIslands, r, c, directions, islandNumber, queue = defaultdict(int), len(grid), len(grid[0]), [(-1, 0), (0, 1), (1, 0), (0, -1)], 2, deque()
        result = 0
        def dfs(i, j):
            if(i < 0 or j < 0 or i == r or j == c or grid[i][j] != 1):
                return 0
            count  =  1
            grid[i][j] = islandNumber
            for x, y in directions:
                count += dfs(x + i, y + j)
            return count
        def getIslandNumber(i, j):
            if(i < 0 or j < 0 or i == r or j == c or grid[i][j] == 0):
                return -1
            else:
                return grid[i][j]
        for i in range(r):
            for j in range(c):
                if(grid[i][j] == 1):
                    distinctIslands[islandNumber] = dfs(i, j)
                    result = max(result,  distinctIslands[islandNumber])
                    islandNumber += 1
                elif(grid[i][j] == 0):
                    queue.append((i, j))
        while(queue):
            x, y = queue.popleft()
            count, considered = 1, []
            for i, j in directions:
                num = getIslandNumber(x + i, y + j)
                if(num != -1 and num not in considered):
                    considered.append(num)
                    count +=  distinctIslands[num]
            #print(x, y, count)
            result = max(result, count)
        return result
        
