#User function Template for python3

class Solution:
    

    def tarjans(self, n, adj):
        dis, low, vis,self.time, self.result, stack = [0] * n, [0] * n, [0] * n, 0, [], []
        def dfs(source):
            dis[source] = low[source] = self.time
            self.time += 1
            stack.append(source)
            vis[source] = 1
            for child in adj[source]:
                if(vis[child] == 0):
                    dfs(child)
                    low[source] = min(low[source], low[child])
                elif(vis[child] == 1):
                    low[source] = min(low[source], dis[child])
            if(low[source] == dis[source]):
                scc = []
                while(stack[-1] != source):
                    vis[stack[-1]] = 2
                    scc.append(stack.pop())
                scc.append(stack.pop())
                self.result.append(sorted(scc))
                vis[source] = 2
        for i in range(n):
            if(vis[i] == 0):
                dfs(i)
        return sorted(self.result)
        





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
        
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        ob = Solution()
        
        ptr = ob.tarjans(V, adj)
        
        for i in range(len(ptr)):
            for j in range(len(ptr[i])):
                if j==len(ptr[i])-1:
                    print(ptr[i][j],end="")
                else:
                    print(ptr[i][j],end=" ")
            print(",",end="")
        print()
# } Driver Code Ends