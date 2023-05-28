---
title: Floki the Boat Builder
tags:
  - Tree
  - Contest
---

## Problem Statement

Floki the boat builder is building boats for Ragnar Lodbrok using a unique tree which is rooted at 0 and has N nodes. Each node i has a value val[i] associated with it.

Floki selects two nodes of the tree, X and Y, for making a boat. The build process will only be successful if X and Y belong to different subtrees and the GCD of (GCD of X subtree and GCD of Y subtree) are known to Floki.
If X and Y given to you are from different subtrees find the final GCD of subtrees. Otherwise, return -1.

**Your Task:**    
You don't need to read input or print anything. Complete the function **gcdTree()** which takes **N, X, Y**, a list of pairs of {start,end} denoting the **edges** and a list of integers **val\[\]** containing the value of each node in the tree, as input parameters and returns the GCD of subtrees or -1.

**Constraints:**  
2 ≤ N ≤ 10<sup>5</sup>  
Number of edges = N - 1  
0 ≤ val\[i\] ≤ 10<sup>5</sup>

## Solution

```py
from math import gcd
from collections import defaultdict
class Solution:
    def gcdTree(self, n, edges, val, x, y):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        def find_gcd(source):
            if(len(adj[source]) == 0):
                return val[source]
            result = val[source]
            for child in adj[source]:
                result = gcd(result, find_gcd(child))
            return result
        def lca(source):
            found_x, found_y = False, False
            if(source == x or source == y):
                return source
            for child in adj[source]:
                node_id = lca(child)
                if(node_id == x):
                    found_x = True
                if(node_id == y):
                    found_y = True
            if(found_x and found_y):
                return source
            if(found_x or found_y):
                return x if(found_x) else y
            return None
        lca_node = lca(0)
        if(lca_node == x or lca_node == y):
            return -1
        return gcd(find_gcd(x), find_gcd(y))
```
