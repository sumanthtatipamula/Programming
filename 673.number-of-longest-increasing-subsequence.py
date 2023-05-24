#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (42.50%)
# Total Accepted:    145.1K
# Total Submissions: 337.2K
# Testcase Example:  '[1,3,5,4,7]'
#
# Given an integer array nums, return the number of longest increasing
# subsequences.
# 
# Notice that the sequence has to be strictly increasing.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1,
# 3, 5, 7].
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there
# are 5 increasing subsequences of length 1, so output 5.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2000
# -10^6 <= nums[i] <= 10^6
# 
# 
#

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[0] * 2] * len(nums)
        max_length, max_count = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            curr_length, curr_count = 1, 1
            for j in range(i + 1, len(nums)):
                if(nums[i] >= nums[j]):
                    continue
                length, count = dp[j]
                if(length + 1 > curr_length):
                    curr_length = length + 1
                    curr_count  =  count
                elif(length + 1 == curr_length):
                    curr_count += count
            dp[i] = [curr_length, curr_count]
            if(curr_length > max_length):
                max_length = curr_length
                max_count = curr_count
            elif(curr_length == max_length):
                max_count += curr_count
        return max_count
        
