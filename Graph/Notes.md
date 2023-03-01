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

1. **Kruskal Algorithm**:

   1. Among all edges that don't create cycles, pick the edge with the least weight
   2. Time Complexity: $O(E. log E)$. Here E represents the number of edges
   3. Space Complexity : O(v)

2. **Prims Algorithms**
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
3. **Back Edges**
   1. It is an edge (u, v) such that v is an ancestor of node u but not part of the DFS Traversal of the tree. Edge from 5 to 4 is a back edge.
   2. The presence of a back edge indicates a cycle in a graph.
   3. Special Property of Ancestors and DFS
      1. Ancestor has to be in call stack when I reach child node.
   4. In Directed Graph
      1. States:
         1. 0 - yet to be visited
         2. 1 - visited and in call stack
         3. 2 - visited and not in call stack
4. **Articulation Points**
   1. Requirements - DFS, Back Edges, DP
   2. A vertex V in a connected graph is a articulation point if and only if the deletion of vertex V together with all edges to V disconnects the graph into two or more non empty components.
   3. _Bridge_: An edge in connected graph if and only if removing it disconnects the graph.
   4. The root of G is an articulation point of G if and only if it has atleast two children
   5. V be a non root vertex of G, then V is articulation point of G if and only if v has a child s such that there is no back edge from s or any descendant of s to a proper ancestor of v.
   6. _Discovered time_: Time at which current node was discovered during the bfs
   7. _Lowest Time_ : It is the minimum discovered time of a node to which we can traverse by using at most one backedge in current subtree.
   8. Conditions:
      1. low[x] >= disc[curr] - articulation point
      2. low[x] > disc[curr] - bridge
5. Shortest Path Algorithms
   1. Single Source Shortest Path
      1. BFS - doesn't work with weighted edges
      2. [Dijkstra Algorithm](https://www.youtube.com/watch?v=Sj5Z-jaE2x0)
         1. doesn't work with negative edges
         2. Greedy algorithm
         3. Algorithm:
            1. Maintain a set of processed nodes
            2. Assign all nodes with distance value = inf except source node 0
            3. Repeat following for (V - 1):
               1. Pick minimum value vertex which is not already processed
               2. Include this selected node in processed set
               3. update all the adjacent node distances
               4. if(new distance < old distance) then update else skip
      3. Bellman Ford
   2. All Pairs shortest Path
      1. Floyd Warshall
      2. Dynamic Programming based algorithm
6. Topological Order and Strongly Connected Components
   1. Topological Sorting : for Directed Acyclic Graph is a linear ordering of vertices such that for every directed edge U V, vertex U comes before V in the ordering. Topological Sorting for a graph is not possible, if it is not a DAG.
   2. Topological Order: You have to number the vertices so that every edge leads from the vertex with a smaller number assigned to the vertex with a larger one.
   3. In other words, you want to find a permutation of the vertices which corresponds to the order defined by all edges of graph.
   4. Topological Order can be non-unique
   5. Topological Order may not exist at all if the graph contains cycles.
   6. There is a difference between DFS and Topological Ordering
   7. Strongly connected components is for Directed Graphs
   8. Terms for Topological Ordering
      1. Finish Time - Time when we leave the node in BFS
      2. For any two nodes u and v, if there is an edge from u -> v finish time of u will be higher than finish time of v
   9. Strongly connected Components
      1. Connectivity in an undirected graph means that every vertex can reach every other vertex via any path. If graph is not connected the graph can broken down into Connected Components
      2. Strong Connectivity applies only to directed graphs. A directed graph is strongly connected if there is a directed path from any vertex to every other vertex
         1. cycle in directed graph is strongly connected component
      3. Condensed Component Graph - is a DAG in which every node is a strongly connected component and edges between nodes if there is an edge from one of the nodes of these SCC in original graph
         1. Considering Strongly connected component as single node.
      4. Source - Node with no incoming edges
      5. Sink - Node with no out going edges
      6. There will be no cycle/SCC in new condensed component graph.
      7. Single Node is a strongly connected component
      8. Reverse of SCC is still SCC same goes with non scc
   10. Kosaraju Algorithm
       1. Algorithm:
          1. Perform DFS traversal of graph. Push Node to stack before returning
          2. Find the transpose graph by reversing the edges
          3. Pop nodes one by one from stack and again do dfs on modified graph
             1. Each Successfull DFS gives 1 SCC
7. Euler Tours
   1. Prerequisites: Segment Tree, Segment Tree with lazy propagation, Fenwick Tree
   2. An euler path is a path that goes through every edge of a graph exactly once.
   3. An Euler circuit is an euler path that begins and ends at the same vertex.
   4. Types
      1. Goto node print it, exit node print it 2 \* nodes
         1. All nodes that lies in timein[u] -> timeout[u] are in subtree of u
         2. To check u is an ancestor v
            1. tin[u] < tin[v] and tout[u] > tout[v]
         3. Sum of all nodes in a subtree
            1. sum(tin[u] + tin[out]) / 2
      2. goto node print it, come back print it 2 \* n - 1
      3. Best Euler Tour
         1. goto node print it(increment time and assign it)
         2. when I leave a node I won't increment time
8. LCA
   1. Binary Lift
9. Re routing of Trees
   1. Initially all vertices are white on the first turn of the game you choose one vertex and paint it black, this becomes the root node of the tree. Then on each turn you choose a white vertex adjacent(connected by an edge) to any black vertex and paint it black. Each time when you choose a vertex(even during the first turn), you gain the number of points equal to the size of connected components consisting only of white vertices that contains the chosen vertex. The game ends when all vertices are painted black. Your task is to maximize the number of points you gain.
10. DeBrujin Sequence
    1. To generate a sequence for base - k of substring size n = 2 we need an overall string of k ^ n
    2. This can be solved using graph theory
    3. Nodes will represent each possible substring of sie N
    4. Edges will be established between Node A and Node B if the last N - 1 digits in Node A when appended with [0..K-1] is transformed into Node B
    5. Use DFS to find a path that visits all nodes exactly once.
    6. Because we always reuse previous n -1 digits to compute the new node we need to get rid of n - 1 adjacent digits k ^ n - 1 times
11. A cycle that travels exactly once over each edge in a graph is called “Eulerian.” A cycle that travels exactly once over each vertex in a graph is called “Hamiltonian.”
