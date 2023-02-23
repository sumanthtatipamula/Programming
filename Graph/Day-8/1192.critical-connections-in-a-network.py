#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#
# https://leetcode.com/problems/critical-connections-in-a-network/description/
#
# algorithms
# Hard (54.55%)
# Total Accepted:    193.4K
# Total Submissions: 354.2K
# Testcase Example:  '4\n[[0,1],[1,2],[2,0],[1,3]]'
#
# There are n servers numbered from 0 to n - 1 connected by undirected
# server-to-server connections forming a network where connections[i] = [ai,
# bi] represents a connection between servers ai and bi. Any server can reach
# other servers directly or indirectly through the network.
# 
# A critical connection is a connection that, if removed, will make some
# servers unable to reach some other server.
# 
# Return all critical connections in the network in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# 
# 
# Example 2:
# 
# 
# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 10^5
# n - 1 <= connections.length <= 10^5
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated connections.
# 
# 
#
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        vis, low, dis, adj = [False] * n, [0] * n, [0] * n, defaultdict(list)
        self.time = 0
        result = []
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(source, parent):
            vis[source] = True
            dis[source] = low[source] = self.time
            self.time += 1
            for child in adj[source]:
                if(not vis[child]):
                    dfs(child, source)
                    low[source] = min(low[child], low[source])
                    if(low[child] > dis[source]):
                        result.append([source, child])
                elif(child != parent):
                    low[source] = min(low[source], dis[child])
        dfs(0, -1)
        return result
        
