#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
#
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
#
# algorithms
# Medium (58.64%)
# Total Accepted:    114K
# Total Submissions: 193.7K
# Testcase Example:  '4\n[[0,1],[0,2],[1,2]]'
#
# There are n computers numbered from 0 to n - 1 connected by ethernet cables
# connections forming a network where connections[i] = [ai, bi] represents a
# connection between computers ai and bi. Any computer can reach any other
# computer directly or indirectly through the network.
# 
# You are given an initial computer network connections. You can extract
# certain cables between two directly connected computers, and place them
# between any pair of disconnected computers to make them directly connected.
# 
# Return the minimum number of times you need to do this in order to make all
# the computers connected. If it is not possible, return -1.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1
# Explanation: Remove cable between computer 1 and 2 and place between
# computers 1 and 3.
# 
# 
# Example 2:
# 
# 
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
# Output: -1
# Explanation: There are not enough cables.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# 1 <= connections.length <= min(n * (n - 1) / 2, 10^5)
# connections[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no repeated connections.
# No two computers are connected by more than one cable.
# 
# 
#
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if(len(connections) < n - 1):
            return -1
        adj, vis = defaultdict(list), [False] * n
        def dfs(source):
            if(vis[source]):
                return 0
            vis[source] = True
            for vertex in adj[source]:
                dfs(vertex)
            return 1
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        return sum([dfs(i) for i in range(n) if(not vis[i])]) - 1
        
