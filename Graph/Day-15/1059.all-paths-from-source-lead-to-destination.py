#
# @lc app=leetcode id=1059 lang=python3
#
# [1059] All Paths from Source Lead to Destination
#
# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/description/
#
# algorithms
# Medium (39.79%)
# Total Accepted:    50.1K
# Total Submissions: 126.8K
# Testcase Example:  '3\n[[0,1],[0,2]]\n0\n2'
#
# Given the edges of a directed graph where edges[i] = [ai, bi] indicates there
# is an edge between nodes ai and bi, and two nodes source and destination of
# this graph, determine whether or not all paths starting from source
# eventually, end at destination, that is:
# 
# 
# At least one path exists from the source node to the destination node
# If a path exists from the source node to a node with no outgoing edges, then
# that node is equal to destination.
# The number of possible paths from source to destination is a finite number.
# 
# 
# Return true if and only if all roads from source lead to destination.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
# Output: false
# Explanation: It is possible to reach and get stuck on both node 1 and node
# 2.
# 
# 
# Example 2:
# 
# 
# Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
# Output: false
# Explanation: We have two possibilities: to end at node 3, or to loop over
# node 1 and node 2 indefinitely.
# 
# 
# Example 3:
# 
# 
# Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# 0 <= edges.length <= 10^4
# edges.length == 2
# 0 <= ai, bi <= n - 1
# 0 <= source <= n - 1
# 0 <= destination <= n - 1
# The given graph may have self-loops and parallel edges.
# 
# 
#
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for u,v in edges:
            if(v not in adj[u]):
                adj[u].append(v)
        vis, leads = [False] * n, [False] * n
        def dfs(current):
            if(vis[current]):
                return leads[current]
            if(current == destination):
                return True
            vis[current] = True
            leadsToDest = False
            for child in adj[current]:
                if(not dfs(child)):
                    leadsToDest = False
                    break
                else:
                    leadsToDest = True
            leads[current] = leadsToDest
            return leadsToDest
        return dfs(source)
        
