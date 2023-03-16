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
        mem = {}
        def traverse(index, target):
            if(target == 0):
                prod = 1.0
                for i in range(index, len(prob)):
                    prod *= 1 - prob[i]
                return prod
            if(index == len(prob)):
                return 0
            if((index, target) in mem):
                return mem[(index, target)]
            result = prob[index] * traverse(index + 1, target - 1)
            result += (1 - prob[index]) * traverse(index + 1, target)
            mem[(index, target)] = result
            return result
        return traverse(0, target)
    
    def rob(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        def robTheHouse(nums):
            dp = [0] * (len(nums) + 1)
            dp[0], dp[1] = 0, nums[0]
            for i in range(1, len(nums)):
                dp[i + 1] =  max(nums[i] + dp[i - 1], dp[i])
            return dp[len(nums)]
        return max(robTheHouse(nums[0: -1]), robTheHouse(nums[1:]))