#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (44.38%)
# Total Accepted:    357.9K
# Total Submissions: 802.8K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# 
# 
# Example 2:
# 
# 
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
# 
# 
#
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue,r,c, result = deque(), len(mat), len(mat[0]), [[float("Inf") for j in range(len(mat[0]))] for  i  in range(len(mat))]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(r):
            for j in range(c):
                if(mat[i][j] == 0):
                    queue.append([i,j])
                else:
                    mat[i][j] = -1
        while(queue):
            x, y = queue.popleft()
            for i, j in directions:
                new_x  = x + i
                new_y  = y + j
                if(new_x  < 0 or new_y < 0 or new_x == r or new_y == c or mat[new_x][new_y] > -1):
                    continue
                mat[new_x][new_y] = 1 + mat[x][y]
                queue.append([new_x, new_y])
        return mat
            
        
