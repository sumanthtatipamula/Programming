"""
You are given an integer array `nums`. You must perform **exactly one** operation where you can **replace** one element `nums[i]` with `nums[i] * nums[i]`. 

Return _the **maximum** possible subarray sum after **exactly one** operation_. The subarray must be non-empty.

**Example 1:**

```
Input: nums = [2,-1,-4,-3]
Output: 17
Explanation: You can perform the operation on index 2 (0-indexed) to make nums = [2,-1,16,-3]. Now, the maximum subarray sum is 2 + -1 + 16 = 17.
```

**Example 2:**

```
Input: nums = [1,-1,1,1,-1,-1,1]
Output: 4
Explanation: You can perform the operation on index 1 (0-indexed) to make nums = [1,1,1,1,-1,-1,1]. Now, the maximum subarray sum is 1 + 1 + 1 + 1 = 4.
```

**Constraints:**

-   `1 <= nums.length <= 10<sup>5</sup>`
-   `-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>`
"""
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
       result = 0
       dp = [0, 0]
       for i in range(0, len(nums)):
           dp[1] = max(nums[i] * nums[i] + dp[0] , dp[1] + nums[i])
           dp[0] = max(0, dp[0] + nums[i])
           result = max(result, dp[1])
       return result