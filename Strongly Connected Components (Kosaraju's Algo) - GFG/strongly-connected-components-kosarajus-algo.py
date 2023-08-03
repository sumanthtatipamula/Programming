#User function Template for python3
from collections import defaultdict
class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, n, adj):
        topological_order = []
        vis = [False] * (n)
        def topological_sorting(source):
            vis[source] = True
            for child in adj[source]:
                if(not vis[child]):
                    topological_sorting(child)
            topological_order.append(source)
        
        for i in range(n):
            if(not vis[i]):
                topological_sorting(i)
        
        RG = defaultdict(list)
        for u in range(n):
            for v in adj[u]:
                RG[v].append(u)
                
        
        vis = [False] * n
        count = 0
        def find_scc(source):
            vis[source] = True
            for child in RG[source]:
                if(not vis[child]):
                    find_scc(child)
        
        while(topological_order):
            node = topological_order.pop()
            if(not vis[node]):
                count += 1
                find_scc(node)
        
        return count
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
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
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends