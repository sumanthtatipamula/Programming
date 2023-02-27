#
# @lc app=leetcode id=2316 lang=python3
#
# [2316] Count Unreachable Pairs of Nodes in an Undirected Graph
#
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
#
# algorithms
# Medium (38.63%)
# Total Accepted:    21.3K
# Total Submissions: 55K
# Testcase Example:  '3\n[[0,1],[0,2],[1,2]]'
#
# You are given an integer n. There is an undirected graph with n nodes,
# numbered from 0 to n - 1. You are given a 2D integer array edges where
# edges[i] = [ai, bi] denotes that there exists an undirected edge connecting
# nodes ai and bi.
# 
# Return the number of pairs of different nodes that are unreachable from each
# other.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, edges = [[0,1],[0,2],[1,2]]
# Output: 0
# Explanation: There are no pairs of nodes that are unreachable from each
# other. Therefore, we return 0.
# 
# 
# Example 2:
# 
# 
# Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# Output: 14
# Explanation: There are 14 pairs of nodes that are unreachable from each
# other:
# 
# [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
# Therefore, we return 14.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# 0 <= edges.length <= 2 * 10^5
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no repeated edges.
# 
# 
#
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj, vis = defaultdict(list), [False] * n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        totalVertices, result = n, 0
        def dfs(source):
            vis[source] = True
            count = 1
            for child in adj[source]:
                if(not vis[child]):
                    count += dfs(child)
            return count
        for i in range(n):
            if(not vis[i]):
                count = dfs(i)
                totalVertices -= count
                result += count * totalVertices
        return result

        
