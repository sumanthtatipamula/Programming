---
title: PT07X - Vertex Cover
tags:
  - DP
  - Spoj
---

## Problem Statement

You are given an unweighted, undirected tree. Write a program to find a vertex set of minimum size in this tree such that each edge has as least one of its end-points in that set.

[Solve :arrow_upper_right:](https://www.spoj.com/problems/PT07X/){.md-button}

### Input

The first line of the input file contains one integer _N_ --- number of nodes in the tree (0 < _N_ <= 100000). Next _N_\-1 lines contain _N_\-1 edges of that tree --- Each line contains a pair (_u_, _v_) means there is an edge between node _u_ and node _v_ (1 <= _u_,_v_ <= _N_).

### Output

Print number of nodes in the satisfied vertex set on one line.

### Example 1

```
Input:
3
1 2
1 3

Output:
1

Explanation:
The set can be {1}

```

### Example 2

```
Input:
3
1 2
2 3

Output:
1

Explanation:
The set can be {2}

```

## Explanation

1. For every node we have 2 options, we include it in the set or not
2. dp[curr][0] -> vertex cover if current node is not in the set of the subtree
3. dp[curr][1] -> vertex cover if the current node is chosen in the set of the subtree
4. for leaf nodes dp[leaf][0] = 0 dp[leaf][1] = 1

## Solution

```py

from collections import defaultdict

n = int(input())
adj = defaultdict(list)
dp = [[0] * 2 for _ in range(n + 1)]
def find_min_vertex(source, parent):
    dp[source][0] = 0
    dp[source][1] = 1
    for child in adj[source]:
        if(child != parent):
            find_min_vertex(child, source)
            dp[source][0] += dp[child][1]
            dp[source][1] += min(dp[child][0], dp[child][1])


for i in range(n -  1):
    u, v =  map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

find_min_vertex(1, -1)
print(min(dp[1][1], dp[1][0]))

```
