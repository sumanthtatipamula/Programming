"""
here are `n` houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house `i`, we can either build a well inside it directly with cost `wells[i - 1]` (note the `-1` due to **0-indexing**), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array `pipes` where each `pipes[j] = [house1<sub>j</sub>, house2<sub>j</sub>, cost<sub>j</sub>]` represents the cost to connect `house1<sub>j</sub>` and `house2<sub>j</sub>` together using a pipe. Connections are bidirectional, and there could be multiple valid connections between the same two houses with different costs.

Return _the minimum total cost to supply water to all houses_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/05/22/1359_ex1.png)

```
Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.

```

**Example 2:**

```
Input: n = 2, wells = [1,1], pipes = [[1,2,1],[1,2,2]]
Output: 2
Explanation: We can supply water with cost two using one of the three options:
Option 1:
  - Build a well inside house 1 with cost 1.
  - Build a well inside house 2 with cost 1.
The total cost will be 2.
Option 2:
  - Build a well inside house 1 with cost 1.
  - Connect house 2 with house 1 with cost 1.
The total cost will be 2.
Option 3:
  - Build a well inside house 2 with cost 1.
  - Connect house 1 with house 2 with cost 1.
The total cost will be 2.
Note that we can connect houses 1 and 2 with cost 1 or with cost 2 but we will always choose the cheapest option. 

```

**Constraints:**

-   `2 <= n <= 10<sup>4</sup>`
-   `wells.length == n`
-   `0 <= wells[i] <= 10<sup>5</sup>`
-   `1 <= pipes.length <= 10<sup>4</sup>`
-   `pipes[j].length == 3`
-   `1 <= house1<sub>j</sub>, house2<sub>j</sub> <= n`
-   `0 <= cost<sub>j</sub> <= 10<sup>5</sup>`
-   `house1<sub>j</sub> != house2<sub>j</sub>`
"""
from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        adj, heap, result, mst = defaultdict(list), [], 0, set()
        for index, cost in enumerate(wells):
            adj[0].append((index + 1, cost))
            heappush(heap, (cost, 0, index + 1))
        for u,v, cost in pipes:
            adj[u].append((v, cost))
            adj[v].append((u, cost))
        mst.add(0)
        while(len(mst) != n + 1):
            cost,u,v  = heappop(heap)
            if(u in mst and v in mst):
                continue
            mst.add(v)
            result += cost
            for child, ccost in adj[v]:
                heappush(heap, (ccost, v, child))
        return result
