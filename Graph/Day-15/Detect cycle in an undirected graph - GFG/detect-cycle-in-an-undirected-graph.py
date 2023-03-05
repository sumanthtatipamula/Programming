from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, n: int, edges: List[List[int]]) -> bool:
	    vis = [-1] * n
	    for i in range(0, n):
	        if(vis[i] == 1):
	            continue
    	    vis[i] = 0
    	    queue = deque([i])
    	    while(queue):
    	        node = queue.popleft()
    	        vis[node] = 1
    	        for child in edges[node]:
    	            if(vis[child] == 1):
                        continue
    	            if(vis[child] == 0):
    	                return True
    	            vis[child] = 0
    	            queue.append(child)
        return False
	            



#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends