#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (46.98%)
# Total Accepted:    329.2K
# Total Submissions: 699.7K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer
# n and a list of edges where edges[i] = [ai, bi] indicates that there is an
# undirected edge between nodes ai and bi in the graph.
# 
# Return true if the edges of the given graph make up a valid tree, and false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2000
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.
# 
# 
#
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph, vis = defaultdict(list), [False] * n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(source, parent):
            if(vis[source]):
                return True
            vis[source] = True
            for child in graph[source]:
                if(vis[child] and child != parent):
                    return False
                if(not dfs(child, source)):
                    return False
            return True
        if(not dfs(0, -1)):
            return False
        for i in range(n):
            if(not vis[i]):
                return False
        return True
        
        
