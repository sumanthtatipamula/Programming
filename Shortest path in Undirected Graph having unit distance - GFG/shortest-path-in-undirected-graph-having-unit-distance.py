#User function Template for python3

from collections import deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        vis, adj, dist, queue = [False] * n, [[] for _ in range(n)], [-1] * n, deque([src])
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis[src],dist[src] = True,0
        while(queue):
            parent = queue.popleft()
            for child in adj[parent]:
                if(vis[child]):
                    continue
                vis[child] = True
                dist[child] = dist[parent] + 1
                queue.append(child)
        return dist
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends