#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
#
# algorithms
# Medium (34.34%)
# Total Accepted:    66K
# Total Submissions: 142.8K
# Testcase Example:  '[2,2,3,-1]\n0\n1'
#
# You are given a directed graph of n nodes numbered from 0 to n - 1, where
# each node has at most one outgoing edge.
# 
# The graph is represented with a given 0-indexed array edges of size n,
# indicating that there is a directed edge from node i to node edges[i]. If
# there is no outgoing edge from i, then edges[i] == -1.
# 
# You are also given two integers node1 and node2.
# 
# Return the index of the node that can be reached from both node1 and node2,
# such that the maximum between the distance from node1 to that node, and from
# node2 to that node is minimized. If there are multiple answers, return the
# node with the smallest index, and if no possible answer exists, return -1.
# 
# Note that edges may contain cycles.
# 
# 
# Example 1:
# 
# 
# Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
# Output: 2
# Explanation: The distance from node 0 to node 2 is 1, and the distance from
# node 1 to node 2 is 1.
# The maximum of those two distances is 1. It can be proven that we cannot get
# a node with a smaller maximum distance than 1, so we return node 2.
# 
# 
# Example 2:
# 
# 
# Input: edges = [1,2,-1], node1 = 0, node2 = 2
# Output: 2
# Explanation: The distance from node 0 to node 2 is 2, and the distance from
# node 2 to itself is 0.
# The maximum of those two distances is 2. It can be proven that we cannot get
# a node with a smaller maximum distance than 2, so we return node 2.
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
# 0 <= node1, node2 < n
# 
# 
#
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        dist, maxd, smallestIndex, distance, vis = {node1: 0}, float("Inf"), float("Inf"), 0, [False] * len(edges)
        while(edges[node1] != -1 and edges[node1] not in dist):
            distance, node1  = distance + 1, edges[node1]
            dist[node1] = distance 
        distance = 0
        while(node2 != -1 and not vis[node2]):
            vis[node2] = True
            if(node2 in dist):
                if(maxd > max(distance, dist[node2])):
                    maxd = max(distance, dist[node2])
                    smallestIndex = node2
                elif(maxd == max(distance, dist[node2])):
                    smallestIndex = min(node2, smallestIndex)
            node2 = edges[node2]
            distance += 1
        return -1 if(maxd == float("Inf")) else smallestIndex
