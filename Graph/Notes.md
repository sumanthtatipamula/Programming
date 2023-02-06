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
8. 