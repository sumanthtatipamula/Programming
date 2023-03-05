#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
#
# algorithms
# Medium (63.95%)
# Total Accepted:    149.3K
# Total Submissions: 233.7K
# Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
#
# You are given an array points representing integer coordinates of some points
# on a 2D-plane, where points[i] = [xi, yi].
# 
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
# absolute value of val.
# 
# Return the minimum cost to make all points connected. All points are
# connected if there is exactly one simple path between any two points.
# 
# 
# Example 1:
# 
# 
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 
# 
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
# 
# 
# 
# Constraints:
# 
# 
# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# All pairs (xi, yi) are distinct.
# 
# 
#
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst, edges, totalCost, adj = set(), [], 0, defaultdict(list)
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        mst.add(0)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = manhattan(points[i], points[j])
                adj[i].append([distance, j])
                adj[j].append([distance, i])
                if(i == 0):
                    edges.append([distance, i,  j])
        heapq.heapify(edges)
        while(len(mst) != len(points)):
            w, u, v = heapq.heappop(edges)
            if(u in mst and v in mst):
                continue
            mst.add(v)
            totalCost += w
            for w, y in adj[v]:
                heapq.heappush(edges, [w, v , y])
        return totalCost

