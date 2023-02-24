"""
You are given an array `nums` of `n` positive integers.

You can perform two types of operations on any element of the array any number of times:

-   If the element is **even**, **divide** it by `2`.
    -   For example, if the array is `[1,2,3,4]`, then you can do this operation on the last element, and the array will be `[1,2,3,2].`
-   If the element is **odd**, **multiply** it by `2`.
    -   For example, if the array is `[1,2,3,4]`, then you can do this operation on the first element, and the array will be `[2,2,3,4].`

The **deviation** of the array is the **maximum difference** between any two elements in the array.

Return _the **minimum deviation** the array can have after performing some number of operations._

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.

```

**Example 2:**

```
Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.

```

**Example 3:**

```
Input: nums = [2,10,8]
Output: 3

```

**Constraints:**

-   `n == nums.length`
-   `2 <= n <= 5 * 10<sup><span>4</span></sup>`
-   `1 <= nums[i] <= 10<sup>9</sup>`
"""

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj, dp, sub, res = defaultdict(list), [0] * n, [0] * n, [0] * n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(source, parent):
            dp[source] = sub[source] = 0
            for child in adj[source]:
                if(child != parent):
                    dfs(child, source)
                    dp[source] +=  dp[child]
                    sub[source] += 1 + sub[child]
            dp[source] += sub[source]
        def dfs1(source, parent):
            res[source] = dp[source]
            for child in adj[source]:
                if(child == parent):
                    continue
                dp[source] -= dp[child]
                dp[source] -= (1 + sub[child])
                sub[source] -= (1 + sub[child])
                dp[child] += dp[source]
                sub[child] += 1 + sub[source]
                dp[child] += 1 + sub[source]
    
                dfs1(child, source)

                dp[child] -= 1 + sub[source]
                sub[child] -= (1 + sub[source])
                dp[child] -= dp[source]
                sub[source] += (1 + sub[child])
                dp[source] += (1 + sub[child])
                dp[source] += dp[child]
        dfs(0, -1)
        dfs1(0, -1)
        return res