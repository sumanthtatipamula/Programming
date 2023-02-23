#
# @lc app=leetcode id=2360 lang=python3
#
# [2360] Longest Cycle in a Graph
#
# https://leetcode.com/problems/longest-cycle-in-a-graph/description/
#
# algorithms
# Hard (38.73%)
# Total Accepted:    17.3K
# Total Submissions: 44.4K
# Testcase Example:  '[3,3,4,2,3]'
#
# You are given a directed graph of n nodes numbered from 0 to n - 1, where
# each node has at most one outgoing edge.
# 
# The graph is represented with a given 0-indexed array edges of size n,
# indicating that there is a directed edge from node i to node edges[i]. If
# there is no outgoing edge from node i, then edges[i] == -1.
# 
# Return the length of the longest cycle in the graph. If no cycle exists,
# return -1.
# 
# A cycle is a path that starts and ends at the same node.
# 
# 
# Example 1:
# 
# 
# Input: edges = [3,3,4,2,3]
# Output: 3
# Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
# The length of this cycle is 3, so 3 is returned.
# 
# 
# Example 2:
# 
# 
# Input: edges = [2,-1,3,1]
# Output: -1
# Explanation: There are no cycles in this graph.
# 
# 
# 
# Constraints:
# 
# 
# n == edges.length
# 2 <= n <= 10^5
# -1 <= edges[i] < n
# edges[i] != i
# 
# 
#
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ancestors, vis = [0] * len(edges), [0] * len(edges)
        adj = defaultdict(list)
        for u, v in enumerate(edges):
            if(v != -1):
                adj[u].append(v)
        self.ans = -1
        def dfs(source, parent):
            if(vis[source] == 2):
                return 
            vis[source] = 1
            ancestors[source] = parent 
            for v in adj[source]:
                if(vis[v] == 0):
                    dfs(v, source)
                elif(vis[v] == 1):
                    count, curr = 1, source
                    while(curr != v):
                        count += 1
                        curr = ancestors[curr]
                    self.ans = max(self.ans, count)
            vis[source] = 2
        
        for i in range(0, len(edges)):
            if(vis[i] == 0):
                dfs(i, -1)
        return self.ans
        
