---
title: Maximum Distance in Arrays
tags:
  - Leetcode
  - Arrays
  - Greedy
  - Premium
---

You are given `m` `arrays`, where each array is sorted in **ascending order**.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers `a` and `b` to be their absolute difference `|a - b|`.

Return _the maximum distance_.

**Example 1:**

```
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

```

**Example 2:**

```
Input: arrays = [[1],[1]]
Output: 0

```

**Constraints:**

- `m == arrays.length`
- `2 <= m <= 10<sup>5</sup>`
- `1 <= arrays[i].length <= 500`
- `-10<sup>4</sup> <= arrays[i][j] <= 10<sup>4</sup>`
- `arrays[i]` is sorted in **ascending order**.
- There will be at most `10<sup>5</sup>` integers in all the arrays.

```py
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_distance = 0
        arrays.sort(key = lambda x: x[0])
        for i in range(1, len(arrays)):
            max_distance = max(max_distance, arrays[i][-1] - arrays[0][0])
        if(len(arrays) > 1):
            max_distance = max(max_distance, arrays[0][-1] - arrays[1][0])
        return max_distance
```
