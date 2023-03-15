#
# @lc app=leetcode id=1770 lang=python3
#
# [1770] Maximum Score from Performing Multiplication Operations
#
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/description/
#
# algorithms
# Hard (36.95%)
# Total Accepted:    91.9K
# Total Submissions: 246.1K
# Testcase Example:  '[1,2,3]\n[3,2,1]'
#
# You are given two 0-indexed integer arrays nums and multipliers of size n and
# m respectively, where n >= m.
# 
# You begin with a score of 0. You want to perform exactly m operations. On the
# i^th operation (0-indexed) you will:
# 
# 
# ⁠   Choose one integer x from either the start or the end of the array nums.
# ⁠   Add multipliers[i] * x to your score.
# ⁠   
# ⁠       Note that multipliers[0] corresponds to the first operation,
# multipliers[1] to the second operation, and so on.
# ⁠   
# ⁠   
# ⁠   Remove x from nums.
# 
# 
# Return the maximum score after performing m operations.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3], multipliers = [3,2,1]
# Output: 14
# Explanation: An optimal solution is as follows:
# - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
# - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
# - Choose from the end, [1], adding 1 * 1 = 1 to the score.
# The total score is 9 + 4 + 1 = 14.
# 
# Example 2:
# 
# 
# Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# Output: 102
# Explanation: An optimal solution is as follows:
# - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the
# score.
# - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
# - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
# - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
# - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
# The total score is 50 + 15 - 9 + 4 + 42 = 102.
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# m == multipliers.length
# 1 <= m <= 300
# m <= n <= 10^5 
# -1000 <= nums[i], multipliers[i] <= 1000
# 
# 
#
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        self.result = 0
        n, m = len(nums), len(multipliers)
       # mem = [[-float("Inf") for _ in range(n)] for _ in range(m)]
        dp =  [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        def traverse(index, left):
            if(index == m):
                return 0
            if(mem[index][left] != -float("Inf")):
                return mem[index][left]
            left_max = multipliers[index] * nums[left]
            left_max += traverse(index + 1, left + 1)
            right_max = multipliers[index] * nums[n - 1 - (index - left)]
            right_max += traverse(index + 1, left)
            mem[index][left] =  max(left_max, right_max)
            return mem[index][left]
        for index in range(m - 1, -1, -1):
            for left in range(index, -1, -1):
                dp[index][left] = max(multipliers[index] * nums[left] + dp[index + 1][left + 1], multipliers[index] * nums[n - 1 - (index - left)] + dp[index + 1][left])
        print(dp)
        return dp[0][0]
        
