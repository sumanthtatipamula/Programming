----
1.  One graph can have atmost k * (k - 1) edges where k is number of vertices
2. There are many representations for graphs, there are two of them are popular
	1. Adjacency Matrix
	2. Adjacency List
3.  Adjacency List comes in handy when  $|E|  \approx |V|^{2}$ or when we need to be able to telll quickly if there is an edges connecting two given vertices
4. If $G$ is a directed graph, the sum of lengths of all the adjacency lists is $|E|$ 
5. If $G$ is an undirected graph, the sum of the lengths of all the adjacency lists is 2 * $|E|$
6. The adjacency list representation has the desirable property that the amount of memory it requires is $\theta(V + E)$
7. Since in an undirected graph, $(u, v)$ and $(v,u)$ represent the same edge, the adjacency matrix $A$ of an undirected graph is its own transpose $A = A^{T}$


## Algorithms
---

1. Kruskal Algorithm:

   1. Among all edges that don't create cycles, pick the edge with the least weight
   2. Time Complexity: $O(E. log E)$. Here E represents the number of edges
   3. Space Complexity : O(v)

2. Prims Algorithms
   1. Weighted Undirected Graph
   2. Greedy Algorithms
   3. Terms:
      1. MST set - all the nodes that have been included in minimum spanning tree
      2. Active Edge - Any edge from a vertex in MST set to V.
      3. MST Edge - An edge that has been included in MST so far
   4. Algorithm:
      1. Start from any Source Vertex.
      2. Out of alk active edges, pick the one with smallest weight
         1. Add Y in MST
         2. Add edges start from Y in active edge list
      3. loop step 2
      4.
