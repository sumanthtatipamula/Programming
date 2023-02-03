#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
#
# algorithms
# Medium (56.11%)
# Likes:    1272
# Dislikes: 103
# Total Accepted:    34.6K
# Total Submissions: 61.3K
# Testcase Example:  '7\n' +
  '[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]\n' +
  '[false,false,true,false,true,true,false]'
#
# Given an undirected tree consisting of n vertices numbered from 0 to n-1,
# which has some apples in their vertices. You spend 1 second to walk over one
# edge of the tree. Return the minimum time in seconds you have to spend to
# collect all apples in the tree, starting at vertex 0 and coming back to this
# vertex.
# 
# The edges of the undirected tree are given in the array edges, where edges[i]
# = [ai, bi] means that exists an edge connecting the vertices ai and bi.
# Additionally, there is a boolean array hasApple, where hasApple[i] = true
# means that vertex i has an apple; otherwise, it does not have any apple.
# 
# 
# Example 1:
# 
# 
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,true,false,true,true,false]
# Output: 8 
# Explanation: The figure above represents the given tree where red vertices
# have an apple. One optimal path to collect all apples is shown by the green
# arrows.  
# 
# 
# Example 2:
# 
# 
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,true,false,false,true,false]
# Output: 6
# Explanation: The figure above represents the given tree where red vertices
# have an apple. One optimal path to collect all apples is shown by the green
# arrows.  
# 
# 
# Example 3:
# 
# 
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,false,false,false,false,false]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai < bi <= n - 1
# fromi < toi
# hasApple.length == n
# 
# 
#

# @lc code=start
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for i in range(n)]
        visited = [False for i in range(n)]
        for edge in edges:
          adj[edge[0]].append(edge[1])
          adj[edge[1]].append(edge[0])
        return self.dfs(adj, 0,0,hasApple, visited)

    def dfs(self, adj, source, depth, hasApple, visited):
        if(visited[source]):
            return 0
        timeForVertex = 2 * depth if(hasApple[source]) else 0
        number_of_apples = 1 if(hasApple[source]) else 0
        visited[source] = True
        for vertex in adj[source]:
            timeForChild = self.dfs(adj, vertex, depth + 1, hasApple, visited)
            if(timeForChild > 0):
                number_of_apples += 1
                timeForVertex += timeForChild
        if(number_of_apples > 1):
            timeForVertex -= (number_of_apples - 1) * 2 * depth
        return timeForVertex

# @lc code=end

