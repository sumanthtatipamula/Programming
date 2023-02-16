#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#
# https://leetcode.com/problems/number-of-closed-islands/description/
#
# algorithms
# Medium (62.71%)
# Total Accepted:    121.4K
# Total Submissions: 189.2K
# Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
#
# <p>Given a 2D&nbsp;<code>grid</code> consists of <code>0s</code>
# (land)&nbsp;and <code>1s</code> (water).&nbsp; An <em>island</em> is a
# maximal 4-directionally connected group of <code><font
# face="monospace">0</font>s</code> and a <em>closed island</em>&nbsp;is an
# island <strong>totally</strong>&nbsp;(all left, top, right, bottom)
# surrounded by <code>1s.</code></p>
# 
# <p>Return the number of <em>closed islands</em>.</p>
# 
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# 
# <p><img alt=""
# src="https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png"
# style="width: 240px; height: 120px;" /></p>
# 
# <pre>
# <strong>Input:</strong> grid =
# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# <strong>Output:</strong> 2
# <strong>Explanation:</strong> 
# Islands in gray are closed because they are completely surrounded by water
# (group of 1s).</pre>
# 
# <p><strong class="example">Example 2:</strong></p>
# 
# <p><img alt=""
# src="https://assets.leetcode.com/uploads/2019/10/31/sample_4_1610.png"
# style="width: 160px; height: 80px;" /></p>
# 
# <pre>
# <strong>Input:</strong> grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# <strong>Output:</strong> 1
# </pre>
# 
# <p><strong class="example">Example 3:</strong></p>
# 
# <pre>
# <strong>Input:</strong> grid = [[1,1,1,1,1,1,1],
# &nbsp;              [1,0,0,0,0,0,1],
# &nbsp;              [1,0,1,1,1,0,1],
# &nbsp;              [1,0,1,0,1,0,1],
# &nbsp;              [1,0,1,1,1,0,1],
# &nbsp;              [1,0,0,0,0,0,1],
# ⁠              [1,1,1,1,1,1,1]]
# <strong>Output:</strong> 2
# </pre>
# 
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# 
# <ul>
# <li><code>1 &lt;= grid.length, grid[0].length &lt;= 100</code></li>
# <li><code>0 &lt;= grid[i][j] &lt;=1</code></li>
# </ul>
# 
#
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if(i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 2):
                return False
            if(grid[i][j] == 1):
                return True
            grid[i][j] = 1
            valid = True
            for k in range(-1, 2, 2):
                valid = valid and dfs(i + k, j) and dfs(i, j + k)
                if(not valid):
                    grid[i][j] = 2
                    return False
            return valid
        result = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if(grid[i][j] == 0 and dfs(i,j)):
                    result += 1
        return result
        
