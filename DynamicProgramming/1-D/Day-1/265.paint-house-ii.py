"""
There are a row of `n` houses, each house can be painted with one of the `k` colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an `n x k` cost matrix costs.

-   For example, `costs[0][0]` is the cost of painting house `0` with color `0`; `costs[1][2]` is the cost of painting house `1` with color `2`, and so on...

Return _the minimum cost to paint all houses_.

**Example 1:**

```
Input: costs = [[1,5,3],[2,9,4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.

```

**Example 2:**

```
Input: costs = [[1,3],[2,4]]
Output: 5

```

**Constraints:**

-   `costs.length == n`
-   `costs[i].length == k`
-   `1 <= n <= 100`
-   `2 <= k <= 20`
-   `1 <= costs[i][j] <= 20`

**Follow up:** Could you solve it in `O(nk)` runtime?
"""
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        min_val = min_color = second_min = None
        for i in range(k):
            if(min_val == None or min_val > costs[-1][i]):
                second_min = min_val
                min_val = costs[-1][i]
                min_color = i
            elif(second_min == None or second_min > costs[-1][i]):
                second_min = costs[-1][i]
   
        for i in range(n - 2, -1, -1):
            tmp_min = tmp_color = tmp_second = None
            for j in range(k):
                cost = costs[i][j] + (min_val if(min_color != j) else second_min)
                if(tmp_min == None or tmp_min > cost):
                    tmp_second = tmp_min
                    tmp_min = cost
                    tmp_color = j
                elif(tmp_second == None or tmp_second > cost):
                    tmp_second = cost
            min_val, min_color, second_min = tmp_min, tmp_color, tmp_second
        #print(second_min)
        return min_val