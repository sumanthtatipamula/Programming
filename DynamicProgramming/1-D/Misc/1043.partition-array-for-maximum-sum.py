#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#
# https://leetcode.com/problems/partition-array-for-maximum-sum/description/
#
# algorithms
# Medium (71.34%)
# Total Accepted:    68.4K
# Total Submissions: 95.7K
# Testcase Example:  '[1,15,7,9,2,5,10]\n3'
#
# Given an integer array arr, partition the array into (contiguous) subarrays
# of length at most k. After partitioning, each subarray has their values
# changed to become the maximum value of that subarray.
# 
# Return the largest sum of the given array after partitioning. Test cases are
# generated so that the answer fits in a 32-bit integer.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: arr becomes [15,15,15,9,10,10,10]
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# Output: 83
# 
# 
# Example 3:
# 
# 
# Input: arr = [1], k = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 500
# 0 <= arr[i] <= 10^9
# 1 <= k <= arr.length
# 
# 
#
class Solution:
    def maxSumAfterPartitioning(self, nums: List[int], k: int) -> int:
        mem = {}
        def traverse(index):
            if(index == len(nums)):
                return 0
            max_so_far = 0
            result = 0
            if(index in mem):
                return mem[index]
            for i in range(index, min(k + index, len(nums))):
                max_so_far = max(max_so_far, nums[i])
                result = max(result, (max_so_far * (i - index + 1)) + traverse(i + 1))
            mem[index] = result
            return result
        return traverse(0)
    
    def maxSumAfterPartitioning(self, nums: List[int], k: int) -> int:
        mem = defaultdict(int)
        for i in range(len(nums)):
            max_val = result = 0
            for j in range(i, i - k, -1):
                if(j < 0):
                    break
                max_val = max(nums[j], max_val)
                result = max(result, (max_val * (i - j + 1)) + mem[j - 1])
            mem[i] = result
        return mem[len(nums) - 1]
