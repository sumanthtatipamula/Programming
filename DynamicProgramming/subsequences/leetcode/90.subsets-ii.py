#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (55.59%)
# Total Accepted:    698.9K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,2]'
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# 
# 
#
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def generate_subsets(index, tmp):
            result.append(tmp[:])
            for i in range(index, len(nums)):
                if(i > index and nums[i] == nums[i - 1]):
                    continue
                tmp.append(nums[i])
                generate_subsets(i + 1, tmp)
                tmp.pop()
        generate_subsets(0, [])
        return result
