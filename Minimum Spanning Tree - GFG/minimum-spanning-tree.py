#User function Template for python3

import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        mst, edges, totalCost = set(), [], 0
        for v, w in adj[0]:
            edges.append((w, 0, v))
        mst.add(0)
        heapq.heapify(edges)
        while(len(mst) != V):
            w, u, v = heapq.heappop(edges)
            if(u in mst and v in mst):
                continue
            mst.add(v)
            totalCost += w
            for y, w in adj[v]:
                heapq.heappush(edges, (w, v , y))
        return totalCost
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends