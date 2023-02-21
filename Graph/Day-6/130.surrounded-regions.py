#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (36.34%)
# Total Accepted:    511.5K
# Total Submissions: 1.4M
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given an m x n matrix board containing 'X' and 'O', capture all regions that
# are 4-directionally surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
# 
# 
# Example 2:
# 
# 
# Input: board = [["X"]]
# Output: [["X"]]
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
# 
# 
#
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions,r,c = [(0,1), (1, 0), (-1, 0), (0,-1)], len(board), len(board[0])
        def dfs(i, j):
            if(i < 0 or j < 0 or i == r or j == c or board[i][j] == 'X' or board[i][j] == 'S'):
                return
            board[i][j] = 'S'
            for k in range(-1,2,2):
                dfs(i + k ,j)
                dfs(i, j + k)
        for i in range(0, c):
            if(board[0][i] == 'O'):
                dfs(0, i)
            if(board[r - 1][i] == 'O'):
                dfs(r - 1, i)
        for j in range(0, r):
            if(board[j][0] == 'O'):
                dfs(j, 0)
            if(board[j][c - 1] == 'O'):
                dfs(j, c- 1)
        for i in range(r):
            for j in range(c):
                if(board[i][j] == 'S'):
                    board[i][j] = 'O'
                elif(board[i][j] == 'O'):
                    board[i][j] = 'X'


        
        
