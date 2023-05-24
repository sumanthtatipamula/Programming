---
title: Refueling
tags:
  - Math
  - Contest
---

## Problem Statement

You're driving a car on the x-axis. But you ran out of fuel **exactly** at point **X**. Luckily, there are refueling stations. For any non-negative integer **K**, there is a refueling station at point **2<sup>K</sup>**. Find the position of your nearest refueling station. If there is more than 1 possible station, return the one present on the right.

[Solve :arrow_upper_right:](https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-103/problems/){.md-button}

**Example 1:**

```
Input:
X = 3,
Output:
4
Explanation:
Nearest station from X = 3 is 2 and
1. Since 4 is present in the rightmost
position therefore 4 is the answer.


```

**Example 2:**

```
Input:
X = 2,
Output:
2
Explanation:
Nearest station from X = 2 is 2.

```

**Your Task:**  
The task is to complete the function **refueling()** which takes an integer **X** as input parameters and returns the position of the nearest refueling station

**Constraints:**  
1 ≤  X ≤ 10<sup>9</sup>

```python

class Solution:
    def refueling(self, position):
        last = 1
        curr = 1
        while(curr < position):
            last = curr
            curr *= 2
        return curr if(abs(curr - position) <= abs(last - position)) else last


```
