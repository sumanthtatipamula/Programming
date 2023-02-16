#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (52.27%)
# Total Accepted:    1.3M
# Total Submissions: 2.5M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# <p>Given an <code>m x n</code> 2D binary grid <code>grid</code> which
# represents a map of <code>&#39;1&#39;</code>s (land) and
# <code>&#39;0&#39;</code>s (water), return <em>the number of
# islands</em>.</p>
# 
# <p>An <strong>island</strong> is surrounded by water and is formed by
# connecting adjacent lands horizontally or vertically. You may assume all four
# edges of the grid are all surrounded by water.</p>
# 
# <p>&nbsp;</p>
# <p><strong>Example 1:</strong></p>
# 
# <pre>
# <strong>Input:</strong> grid = [
# ⁠ [&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;0&quot;],
# ⁠ [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;],
# ⁠ [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
# ⁠ [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;]
# ]
# <strong>Output:</strong> 1
# </pre>
# 
# <p><strong>Example 2:</strong></p>
# 
# <pre>
# <strong>Input:</strong> grid = [
# ⁠ [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
# ⁠ [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
# ⁠ [&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;],
# ⁠ [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;1&quot;]
# ]
# <strong>Output:</strong> 3
# </pre>
# 
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# 
# <ul>
# <li><code>m == grid.length</code></li>
# <li><code>n == grid[i].length</code></li>
# <li><code>1 &lt;= m, n &lt;= 300</code></li>
# <li><code>grid[i][j]</code> is <code>&#39;0&#39;</code> or
# <code>&#39;1&#39;</code>.</li>
# </ul>
# 
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if(i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == "0"):
                return True
            grid[i][j] = '0'
            for k in range(-1, 2, 2):
                dfs(i + k, j)
                dfs(i, j + k)
        result = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if(grid[i][j] == '1'):
                    result += 1
                    dfs(i,j)
        return result
        
