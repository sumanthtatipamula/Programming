#
# @lc app=leetcode id=1135 lang=python3
#
# [1135] Connecting Cities With Minimum Cost
#
# https://leetcode.com/problems/connecting-cities-with-minimum-cost/description/
#
# algorithms
# Medium (61.22%)
# Total Accepted:    65K
# Total Submissions: 106.1K
# Testcase Example:  '3\n[[1,2,5],[1,3,6],[2,3,1]]'
#
# There are n cities labeled from 1 to n. You are given the integer n and an
# array connections where connections[i] = [xi, yi, costi] indicates that the
# cost of connecting city xi and city yi (bidirectional connection) is costi.
# 
# Return the minimum cost to connect all the n cities such that there is at
# least one path between each pair of cities. If it is impossible to connect
# all the n cities, return -1,
# 
# The cost is the sum of the connections' costs used.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
# Output: 6
# Explanation: Choosing any 2 edges will connect all cities so we choose the
# minimum 2.
# 
# 
# Example 2:
# 
# 
# Input: n = 4, connections = [[1,2,3],[3,4,4]]
# Output: -1
# Explanation: There is no way to connect all cities even if all edges are
# used.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# 1 <= connections.length <= 10^4
# connections[i].length == 3
# 1 <= xi, yi <= n
# xi != yi
# 0 <= costi <= 10^5
# 
# 
#
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key = lambda x: x[-1])
        parent, rank, edges, totalCost = [i for i in range(n + 1)], [1] * (n + 1), n, 0
        def find(x):
            if(parent[x] == x):
                return x
            parent[x] = find(parent[x])
            return parent[x]
        for x,y, cost in connections:
            rootx = find(x)
            rooty = find(y)
            if(rootx != rooty):
                totalCost += cost
                edges -= 1
                if(rank[rootx] > rank[rooty]):
                    parent[rooty] = rootx
                elif(rank[rooty] > rank[rootx]):
                    parent[rootx] = rooty
                else:
                    rank[rootx] += 1
                    parent[rooty] = rootx
            if(edges == 1):
                return totalCost
        return -1
        
