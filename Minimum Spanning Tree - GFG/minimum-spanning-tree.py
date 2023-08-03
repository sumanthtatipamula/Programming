#User function Template for python3

from heapq import heappush, heappop

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, n, adj):
        queue, cost, mst = [], 0, set()
        heappush(queue, [0, 0])
        while(len(mst) < n):
            node = heappop(queue)
            if(node[-1] in mst):
                continue
            cost += node[0]
            mst.add(node[-1])
            for v, w in adj[node[-1]]:
                if(v not in mst):
                    heappush(queue, [w, v])
        return cost    
        


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