#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#
# https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
#
# algorithms
# Medium (42.94%)
# Total Accepted:    93.4K
# Total Submissions: 192.4K
# Testcase Example:  '3\n[[0,1],[1,2]]\n[]'
#
# You are given an integer n, the number of nodes in a directed graph where the
# nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph,
# and there could be self-edges and parallel edges.
# 
# You are given two arrays redEdges and blueEdges where:
# 
# 
# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node
# ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from
# node uj to node vj in the graph.
# 
# 
# Return an array answer of length n, where each answer[x] is the length of the
# shortest path from node 0 to node x such that the edge colors alternate along
# the path, or -1 if such a path does not exist.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
# 
# 
# Example 2:
# 
# 
# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 100
# 0 <= redEdges.length, blueEdges.length <= 400
# redEdges[i].length == blueEdges[j].length == 2
# 0 <= ai, bi, uj, vj < n
# 
# 
#
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj, res, vis = defaultdict(list), [-1] * n, set()
        for u, v in redEdges:
                adj[u].append([v, 'R'])
        for u,v in blueEdges:
                adj[u].append([v, 'B'])
        res[0] = 0
        queue = deque([[0, 'R'], [0, 'B']])
        level = 0
        while(queue):
            level += 1
            for _ in range(len(queue)):
                source, edgeType = queue.popleft()
                for child, childEdgeType in adj[source]:
                    edgeKey = str(source) + childEdgeType+ str(child)
                    if(childEdgeType != edgeType and edgeKey not in vis):
                        vis.add(edgeKey)
                        if(res[child] == -1):
                            res[child] = level
                        queue.append([child, childEdgeType])
        return res
