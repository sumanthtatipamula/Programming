#User function Template for python3

from collections import defaultdict
class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, v, adj):
        stack, result, vis = [], 0, [False] * v
        def dfs(adj, source, vis, stack = []):
            vis[source] = True
            for child in adj[source]:
                if(not vis[child]):
                    dfs(adj, child, vis, stack)
            stack.append(source)
        for i in range(0, v):
            if(not vis[i]):
                dfs(adj, i, vis, stack)
        transpose = defaultdict(list)
        for i in range(0, v):
            for j in adj[i]:
                transpose[j].append(i)
        adj = transpose
        vis = [False] * v
        #print(stack, vis)
        while(stack):
            index = stack.pop()
            if(not vis[index]):
                dfs(transpose, index, vis)
                result += 1
        return result
        


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