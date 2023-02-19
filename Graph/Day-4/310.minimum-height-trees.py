#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
# https://leetcode.com/problems/minimum-height-trees/description/
#
# algorithms
# Medium (38.53%)
# Total Accepted:    239.9K
# Total Submissions: 622.6K
# Testcase Example:  '4\n[[1,0],[1,2],[1,3]]'
#
# A tree is an undirected graph in which any two vertices are connected by
# exactly one path. In other words, any connected graph without simple cycles
# is a tree.
# 
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
# where edges[i] = [ai, bi] indicates that there is an undirected edge between
# the two nodes ai and bi in the tree, you can choose any node of the tree as
# the root. When you select a node x as the root, the result tree has height h.
# Among all possible rooted trees, those with minimum height (i.e. min(h))  are
# called minimum height trees (MHTs).
# 
# Return a list of all MHTs' root labels. You can return the answer in any
# order.
# 
# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node
# with label 1 which is the only MHT.
# 
# 
# Example 2:
# 
# 
# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2 * 10^4
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# All the pairs (ai, bi) are distinct.
# The given input is guaranteed to be a tree and there will be no repeated
# edges.
# 
# 
#
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if(not edges):
            return [0]
        elements, queue, graph, degree, result = n, deque(), defaultdict(list), [0] * n, []
        for u, v in edges:
            degree[v] += 1
            degree[u] += 1
            graph[v].append(u)
            graph[u].append(v)
        [queue.append(i) for i in range(n) if(degree[i] == 1)]
        while(elements > 2):
            elements -= len(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in graph[node]:
                    degree[child] -= 1
                    if(degree[child] == 1):
                        queue.append(child)
        return list(queue)
