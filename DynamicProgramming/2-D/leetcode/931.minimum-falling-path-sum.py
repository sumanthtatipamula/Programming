#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
# https://leetcode.com/problems/minimum-falling-path-sum/description/
#
# algorithms
# Medium (69.13%)
# Total Accepted:    236.3K
# Total Submissions: 341.9K
# Testcase Example:  '[[2,1,3],[6,5,4],[7,8,9]]'
#
# Given an n x n array of integers matrix, return the minimum sum of any
# falling path through matrix.
# 
# A falling path starts at any element in the first row and chooses the element
# in the next row that is either directly below or diagonally left/right.
# Specifically, the next element from position (row, col) will be (row + 1, col
# - 1), (row + 1, col), or (row + 1, col + 1).
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
# 
# 
# 
# Constraints:
# 
# 
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
# 
# 
#
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r, c, mem = len(matrix), len(matrix[0]), {}
        def recursive(i, j):
            if(i < 0 or j < 0 or i == r or j == c):
                return float("Inf")
            if((i, j) in mem):
                return mem[(i, j)]
            if(i == r - 1):
                return matrix[i][j]
            mem[(i, j)] = matrix[i][j] + min([recursive(i + 1, j + y) for y in range(-1, 2)])
            return mem[(i, j)]
        # return min([recursive(0, j) for j in range(c)])
        dp = matrix[-1]
        for i in range(r - 2, -1, -1):
            for j in range(c):
                if(j == 0):
                    matrix[i][j] += min(dp[j], dp[j + 1])
                elif(j == c - 1):
                    matrix[i][j] += min(dp[j - 1], dp[j])
                else:
                    matrix[i][j] += min(dp[j - 1], dp[j], dp[j + 1])
            dp = matrix[i]
        return min(matrix[0])
                

        
