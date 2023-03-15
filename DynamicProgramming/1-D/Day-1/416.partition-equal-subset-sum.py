#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (46.44%)
# Total Accepted:    601.7K
# Total Submissions: 1.3M
# Testcase Example:  '[1,5,11,5]'
#
# Given an integer array nums, return true if you can partition the array into
# two subsets such that the sum of the elements in both subsets is equal or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 
# 
#
class Solution:
    ## Top Down Approach
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) 
        if(total % 2 != 0):
            return False
        required_sum = total // 2
        dp = [[-1] * (required_sum + 1)] * len(nums)
        def traverse(curr_sum, index):
            if(index == len(nums) or curr_sum > required_sum):
                return False
            if(curr_sum + nums[index] == required_sum):
                dp[index][required_sum] = 1
                return True
            if(dp[index][curr_sum] > -1):
                return dp[index][curr_sum] == 1
            dp[index][curr_sum] = 1 if(traverse(curr_sum + nums[index], index + 1) or traverse(curr_sum, index + 1)) else 0
            return dp[index][curr_sum] == 1
        return traverse(0, 0)

    ## Bottom Up Approach
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) 
        if(total % 2 != 0):
            return False
        required_sum = total // 2
        dp = [False] * (required_sum + 1)
        dp[0] = True
        for i in range(1, len(nums) + 1):
            for j in range(required_sum, nums[i - 1] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i - 1]]
        return dp[required_sum]
        
