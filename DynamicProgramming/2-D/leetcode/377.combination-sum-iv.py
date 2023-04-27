#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (52.15%)
# Total Accepted:    356.2K
# Total Submissions: 682.4K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an array of distinct integers nums and a target integer target, return
# the number of possible combinations that add up to target.
# 
# The test cases are generated so that the answer can fit in a 32-bit
# integer.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# 
# 
# Example 2:
# 
# 
# Input: nums = [9], target = 3
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
# 
# 
# 
# Follow up: What if negative numbers are allowed in the given array? How does
# it change the problem? What limitation we need to add to the question to
# allow negative numbers?
# 
#
class Solution(object):
    def combinationSum4(self, nums, target):
        mem = {}
        def count(target):
            if(target <= 0):
                return 1 if(target == 0) else 0
            total = 0
            if(target in mem):
                return mem[target]
            for i in range(0, len(nums)):
                if(nums[i] <= target):
                    total += count(target - nums[i])
            mem[target]  = total
            return total
        result = count(target)
        return result
    
    def combinationSum4(self, nums, target):
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if(i >= num):
                    dp[i] += dp[i - num]
        return dp[target]
        
        
