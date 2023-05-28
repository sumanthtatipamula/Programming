---
title: 2713. Maximum Strictly Increasing Cells in a Matrix
tags:
  - DP
  - Contest
---

## Problem Statement

---

Given a **1-indexed** `m x n` integer matrix `mat`, you can select any cell in the matrix as your **starting cell**.

From the starting cell, you can move to any other cell **in the** **same row or column**, but only if the value of the destination cell is **strictly greater** than the value of the current cell. You can repeat this process as many times as possible, moving from cell to cell until you can no longer make any moves.

Your task is to find the **maximum number of cells** that you can visit in the matrix by starting from some cell.

Return _an integer denoting the maximum number of cells that can be visited._

**Example 1:**

**![](https://assets.leetcode.com/uploads/2023/04/23/diag1drawio.png)**

```
Input: mat = [[3,1],[3,4]]
Output: 2
Explanation: The image shows how we can visit 2 cells starting from row 1, column 2. It can be shown that we cannot visit more than 2 cells no matter where we start from, so the answer is 2.

```

**Example 2:**

**![](https://assets.leetcode.com/uploads/2023/04/23/diag3drawio.png)**

```
Input: mat = [[1,1],[1,1]]
Output: 1
Explanation: Since the cells must be strictly increasing, we can only visit one cell in this example.

```

**Example 3:**

**![](https://assets.leetcode.com/uploads/2023/04/23/diag4drawio.png)**

```
Input: mat = [[3,1,6],[-9,5,7]]
Output: 4
Explanation: The image above shows how we can visit 4 cells starting from row 2, column 1. It can be shown that we cannot visit more than 4 cells no matter where we start from, so the answer is 4.

```

**Constraints:**

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10<sup>5</sup>`
- `1 <= m * n <= 10<sup>5</sup>`
- `-10<sup>5</sup> <= mat[i][j] <= 10<sup>5</sup>`

## Solution

```py
class Solution:
    def maxIncreasingCells(self, grid: List[List[int]]) -> int:
        elements = defaultdict(list)
        n, m = len(grid), len(grid[0])
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                elements[grid[i][j]].append([i, j])
        res = [0] * (n + m)
        dp = [[0] * m for _ in range(n)]
        for element in sorted(elements):
            for i, j in elements[element]:
                dp[i][j] = max(res[i], res[~j]) + 1
            for i, j in elements[element]:
                res[i] = max(res[i], dp[i][j])
                res[~j] = max(res[~j], dp[i][j])
        return max(res)
```
