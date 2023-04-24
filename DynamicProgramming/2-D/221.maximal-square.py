#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (44.71%)
# Total Accepted:    571.9K
# Total Submissions: 1.3M
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given an m x n binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: matrix = [["0"]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
# 
# 
#
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result, r, c = 0, len(matrix), len(matrix[0])
        for i in range(0, r):
            for j in range(0, c):
                matrix[i][j] = ord(matrix[i][j]) - ord('0')
                if(matrix[i][j] == 1):
                    result = 1
        for i in range(1, r):
            for j in range(1, c):
                if(matrix[i][j] == 1):
                    matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1])
                    # print(matrix[i][j])
                    result = max(result, matrix[i][j])
        return result * result
        
