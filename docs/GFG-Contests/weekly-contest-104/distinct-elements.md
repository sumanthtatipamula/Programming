---
title: Distinct Elements
tags:
  - Greedy
  - Contest
---

## Problem Statement

Given an array **A\[ \]** of size **N** and an integer **K**.  
For each **i (0 ≤ i ≤ N - 1)** you can perform **exactly** one of the following operations:

1.  Add **K** to **i<sup>th</sup>** element, **A\[i\].**
2.  Subtract **K** from the **i<sup>th</sup>** element, **A\[i\].**
3.  Leave **i<sup>th</sup>** element, **A\[i\]** as it is.

After performing operations on all elements, you have to count the number of distinct elements in the array.  
You have to find the maximum number of distinct elements you can obtain in the array if you perform operations optimally.

**Example 1:**

```
Input:
N = 6
K = 2
A[] = {2, 4, 3, 2, 2, 1}
Output:
6
Explanation: Subtract K from the first
element, Add K to the second and fourth
element and Leave the third, fifth and
sixth element as it is. After performing
these operations we will obtain A[] =
{0, 6, 3, 4, 2, 1}. Hence, the number of
distinct elements are 6.

```

**Example 2:**

```
Input:
N = 2
K = 1
A[] = {1, 2}
Output:
2
Explanation: All elements are already
distinct.

```

**Your Task:**  
You don't need to read input or print anything. Your task is to complete the function **distinctElements()** which takes the integer **N**, integer **K,** and array **A\[ \]** as input parameters and returns the maximum number of distinct elements.

**Constraints:**  
1 ≤ N, K ≤ 10<sup>5</sup>  
1 ≤ A\[i\] ≤ 10<sup>9</sup>

## Solution

```py
class Solution:
    def distinctElements(self, n, k, arr):
        arr.sort(reverse = True)
        unique = set()
        for element in arr:
            if(element + k not in unique):
                unique.add(element + k)
            elif(element not in unique):
                unique.add(element)
            else:
                unique.add(element - k)
        return len(unique)
```
