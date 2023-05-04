#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (53.35%)
# Total Accepted:    262.1K
# Total Submissions: 489.5K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an integer array nums and an integer k, split nums into k non-empty
# subarrays such that the largest sum of any subarray is minimized.
# 
# Return the minimized largest sum of the split.
# 
# A subarray is a contiguous part of the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum
# among the two subarrays is only 18.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum
# among the two subarrays is only 9.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 10^6
# 1 <= k <= min(50, nums.length)
# 
# 
#
class Solution:
    def splitArray(self, nums, k):
        mem = {}
        def find_min_largest_sum(index, splits):
            if(index == len(nums) and splits == k):
                return 0
            if(index == len(nums) or splits > k):
                return float("Inf")
            if((index, splits) in mem):
                return mem[(index, splits)]
            total, largest_sum = 0, float("Inf")
            for i in range(index, len(nums)):
                total += nums[i]
                val = find_min_largest_sum(i + 1, splits + 1)
                if(val != float("Inf")):
                    largest_sum = min(largest_sum, max(total, val))
            mem[(index, splits)] = largest_sum
            return largest_sum
        return find_min_largest_sum(0, 0)


    def splitArray(self, nums, k):
        left, right = max(nums), sum(nums)
        def isSplitPossible(target):
            splits, total = 1, 0
            for num in nums:
                total += num
                if(total > target):
                    total = num
                    splits += 1
            return splits <= k
        while(left <= right):
            mid = left + (right - left) // 2
            if(isSplitPossible(mid)):
                right  = mid - 1
            else:
                left = mid + 1
        return left



