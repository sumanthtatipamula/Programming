"""
Given an undirected Graph with **N** vertices (Numbered from **1** to **N**) and **M** edges, The task is to count the number of possible triangles. 

  
**Example 1:**

```
Input:
N = 5, M = 4
Edges[][] = {{1,2},{3,2},{1,3},{5,2}}
Output: 1
Explanation: 
    1
  /   \
 3 ___ 2 ___ 5
There is one triangle.

```

**Example 2:**

```
Input:
N = 4, M = 6
Edges[][] = {{1,2},{1,3},{1,4},{2,3},{2,4},{3,4}}
Output: 4
Explanation: Every triplet makes the triangle.
```

  
**Your task:**  
You don’t need to read input or print anything. Your task is to complete the function **countTriangles()** which takes the integer **N** denoting the number of vertices, **M** denoting the number of edges in the graph and 2D array **Edges\[\]\[\]** where as input parameters and returns the count of triangles.

  
**Expected Time Complexity:** O(N<sup>3</sup>)  
**Expected Auxiliary Space:** O(N<sup>2</sup>)

  
**Constraints:**  
1 ≤ N ≤ 10<sup>2</sup>  
0 ≤ M ≤ N\*(N-1)/2
"""
from collections import defaultdict
class Solution:
    def countTriangles(self, N, M, edges):
        adj, mat = [[] for i in range(N + 1)],[[0 for i in range(N + 1)] for j in range(N + 1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            mat[u][v] = 1
            mat[v][u] = 1
        result = 0
        for i in adj:
            for j in range(len(i)):
                for k in range(j + 1, len(i)):
                    if(mat[i[j]][i[k]]):
                        result += 1
        return result // 3

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges = []
        for i in range(M):
            e = list(map(int, input().strip().split()))
            Edges.append(e)
        ob = Solution()
        ans = ob.countTriangles(N, M, Edges)
        print(ans)


# } Driver Code Ends