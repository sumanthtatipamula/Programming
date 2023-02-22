#
# @lc app=leetcode id=2368 lang=python3
#
# [2368] Reachable Nodes With Restrictions
#
# https://leetcode.com/problems/reachable-nodes-with-restrictions/description/
#
# algorithms
# Medium (57.67%)
# Total Accepted:    30.5K
# Total Submissions: 52.7K
# Testcase Example:  '7\n[[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]\n[4,5]'
#
# There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1
# edges.
# 
# You are given a 2D integer array edges of length n - 1 where edges[i] = [ai,
# bi] indicates that there is an edge between nodes ai and bi in the tree. You
# are also given an integer array restricted which represents restricted
# nodes.
# 
# Return the maximum number of nodes you can reach from node 0 without visiting
# a restricted node.
# 
# Note that node 0 will not be a restricted node.
# 
# 
# Example 1:
# 
# 
# Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted =
# [4,5]
# Output: 4
# Explanation: The diagram above shows the tree.
# We have that [0,1,2,3] are the only nodes that can be reached from node 0
# without visiting a restricted node.
# 
# 
# Example 2:
# 
# 
# Input: n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted =
# [4,2,1]
# Output: 3
# Explanation: The diagram above shows the tree.
# We have that [0,5,6] are the only nodes that can be reached from node 0
# without visiting a restricted node.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges represents a valid tree.
# 1 <= restricted.length < n
# 1 <= restricted[i] < n
# All the values of restricted are unique.
# 
# 
#
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj = defaultdict(list)
        restrictedset = set(restricted)
        print(edges)
        for u, v in edges:
            if(u in restrictedset or v in restrictedset):
                continue
            adj[u].append(v)
            adj[v].append(u)
        queue, vis = deque([0]), [False] * n
        count = 0
        vis[0] = True
        while(queue):
            count += 1
            vertex = queue.popleft()
            for child in adj[vertex]:
                if(not vis[child]):
                    vis[child] = True
                    queue.append(child)
        return count


            
        
