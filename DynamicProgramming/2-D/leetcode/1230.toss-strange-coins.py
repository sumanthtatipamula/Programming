"""
You have some coins.  The `i`\-th coin has a probability `prob[i]` of facing heads when tossed.

Return the probability that the number of coins facing heads equals `target` if you toss every coin exactly once.

**Example 1:**

```
Input: prob = [0.4], target = 1
Output: 0.40000

```

**Example 2:**

```
Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
Output: 0.03125

```

**Constraints:**

-   `1 <= prob.length <= 1000`
-   `0 <= prob[i] <= 1`
-   `0 <= target` `<= prob.length`
-   Answers will be accepted as correct if they are within `10^-5` of the correct answer.
"""
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:        
        dp = [[0] * (target + 1) for _ in range(len(prob) + 1)]
        dp[0][0] = 1
        for i in range(1, len(prob) + 1):
            for j in range(0, target + 1):
                dp[i][j] = (1 - prob[i - 1]) * dp[i - 1][j]
                if(i == 4 and j == 2):
                    print(dp[i][j], j)
                if(j > 0):
                    dp[i][j] += max(dp[i][j], prob[i - 1] * dp[i - 1][j - 1])
        return dp[len(prob)][target]