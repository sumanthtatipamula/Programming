#User function Template for python3
from collections import defaultdict
class Solution:
    def check(self, n, m, edges): 
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis = set()
        def dfs(source):
            vis.add(source)
            if(len(vis) == n):
                return True
            for child in adj[source]:
                if(not child in vis and dfs(child)):
                    return True
            vis.remove(source)
            return False
        for i in range(1, n + 1):
            if(dfs(i)):
                return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges=[]
        e = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i],e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends