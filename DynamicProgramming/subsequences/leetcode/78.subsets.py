#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (74.34%)
# Total Accepted:    1.4M
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# 
# 
#
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def generate_subsets(index, tmp):
            if(index == len(nums)):
                result.append(tmp[:])
                return
            generate_subsets(index + 1, tmp)
            tmp.append(nums[index])
            generate_subsets(index + 1, tmp)
            tmp.pop()
        generate_subsets(0, [])
        return result
