---
title: Density of a Tree
tags:
  - Tree
  - Contest
---

## Problem Statement

Given a Tree of **N** nodes numbered from 0 to N-1 rooted at **0**<sup><strong>th</strong> </sup> node, Find density of it upto exactly six decimal places.  
Density of the Tree = Size of the tree / Height of the tree.  
You are given array **par\[ \]** where **par\[i\]** is the parent of **i<sup>th</sup>** node. As **0<sup>th</sup>** node is the root, so **par\[0\] = -1**.

**Example 1:**

```
Input:
N = 3
par[] = {-1, 0, 0}
Output:
1.500000
Explanation:
Given tree:
            0  
          /   \  
         1     2
Size of the tree = 3
Height of the tree = 2
Density of the tree = 3/2 = 1.5

```

**Example 2:**

```
Input:
N = 2
par[] = {-1, 0}
Output:
1.000000
Explanation:
Given tree:
            0  
            |
            1
Size of the tree = 2
Height of the tree = 2
Density of the tree = 2/2 = 1
```

**Your Task:**  
You don't need to read input or print anything. Your task is to complete the function **density( )** which takes number of nodes **N** and array **par\[ \]** as input parameters and returns the density of the tree upto six decimal places.

**Constraints:**  
1 ≤ N ≤ 2\*10<sup>5</sup>  
par\[0\] = -1  
0 ≤ par\[i\] < N and 0 < i < N

## Solution

```py
from collections import defaultdict
class Solution:
    def density(self, n,  par):
        adj = defaultdict(list)
        def height(source):
            max_height = 0
            for v in adj[source]:
                max_height = max(max_height, height(v))
            return 1 + max_height
        for v, u in enumerate(par):
            adj[u].append(v)
        return n / height(0)
```
