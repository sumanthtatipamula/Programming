"""
There are `n` **unique** candies (labeled `1` through `n`) and `k` bags. You are asked to distribute **all** the candies into the bags such that every bag has **at least** one candy.

There can be multiple ways to distribute the candies. Two ways are considered **different** if the candies in one bag in the first way are not all in the same bag in the second way. The order of the bags and the order of the candies within each bag do not matter.

For example, `(1), (2,3)` and `(2), (1,3)` are considered different because candies `2` and `3` in the bag `(2,3)` in the first way are not in the same bag in the second way (they are split between the bags `(2)` and `(1,3)`). However, `(1), (2,3)` and `(3,2), (1)` are considered the same because the candies in each bag are all in the same bags in both ways.

Given two integers, `n` and `k`, return _the **number** of different ways to distribute the candies_. As the answer may be too large, return it **modulo** `10<sup>9</sup> + 7`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/16/candies-1.png)

```
Input: n = 3, k = 2
Output: 3
Explanation: You can distribute 3 candies into 2 bags in 3 ways:
(1), (2,3)
(1,2), (3)
(1,3), (2)

```

**Example 2:**

```
Input: n = 4, k = 2
Output: 7
Explanation: You can distribute 4 candies into 2 bags in 7 ways:
(1), (2,3,4)
(1,2), (3,4)
(1,3), (2,4)
(1,4), (2,3)
(1,2,3), (4)
(1,2,4), (3)
(1,3,4), (2)

```

**Example 3:**

```
Input: n = 20, k = 5
Output: 206085257
Explanation: You can distribute 20 candies into 5 bags in 1881780996 ways. 1881780996 modulo 109 + 7 = 206085257.

```

**Constraints:**

-   `1 <= k <= n <= 1000`
"""
from math import comb
class Solution:
    def waysToDistribute(self, candy: int, k: int) -> int:
        mod = 10 ** 9 + 7
        mem = {}
        def ways(bags, candies):
            if(bags > candies):
                return 0
            if(bags == 1 or candies == bags):
                return 1
            if((bags, candies) in mem):
                return mem[(bags, candies)]
            count = 0
            for i in range(0, (candies - bags) + 1):
                count  = (count + comb(candies - 1, i) * ways(bags - 1, candies - (i + 1)) % mod) % mod
            mem[(bags, candies)] = count
            return count
        return ways(k, candy)

    def waysToDistribute(self, candies: int, bags: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (candies + 1) for _ in range(bags + 1)]
        dp[0][0] = 1
        for i in range(1, bags + 1):
            for j in range(i, candies + 1):
                for k in range(0, (j - i) + 1):
                    dp[i][j] = (dp[i][j] + comb(j - 1, k) * dp[i - 1][j - (k + 1)]) % mod
        return dp[bags][candies]
    
    def waysToDistribute(self, candies: int, bags: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (candies + 1) for _ in range(bags + 1)]
        dp[0][0] = 1
        for i in range(bags + 1):
            dp[i][i] = 1
        for i in range(1, bags + 1):
            for j in range(i + 1, candies + 1):
                dp[i][j] = (dp[i][j] + i * dp[i][j - 1] + dp[i - 1][j - 1]) % mod
        return dp[bags][candies]

