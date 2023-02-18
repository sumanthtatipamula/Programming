#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#
# algorithms
# Medium (62.19%)
# Total Accepted:    323.2K
# Total Submissions: 519.6K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
# You have a graph of n nodes. You are given an integer n and an array edges
# where edges[i] = [ai, bi] indicates that there is an edge between ai and bi
# in the graph.
# 
# Return the number of connected components in the graph.
# 
# 
# Example 1:
# 
# 
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.
# 
# 
#
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph, visited = defaultdict(set), set()
        [(graph[u].add(v), graph[v].add(u)) for u, v in edges]
        def dfs(source):
            if(source in visited):
                return 0
            visited.add(source)
            for child in graph[source]:
                dfs(child)
            return 0
        return sum([1 + dfs(i) for i in range(0,n) if(i not in visited)])
