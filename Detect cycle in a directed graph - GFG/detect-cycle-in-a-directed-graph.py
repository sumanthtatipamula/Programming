#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, v, adj):
        vis = [0] * v
        def isCycle(source, parent):
            if(vis[source] == 2):
                return False
            vis[source] = 1
            cycle = False
            for v in adj[source]:
                if(vis[v] == 0):
                    cycle = cycle or isCycle(v, source)
                else:
                    cycle = cycle or (vis[v] == 1)
            vis[source] = 2
            return cycle
            
        for i in  range(v):
            if(vis[i] == 0 and isCycle(i, -1)):
                return True
        return False
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends