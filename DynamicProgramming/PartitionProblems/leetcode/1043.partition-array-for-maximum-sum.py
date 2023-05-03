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
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        mem = {}
        def makeMaxSum(index, prevPartitionIndex, max_val):
            if(index == len(arr) and (index - prevPartitionIndex) <= k):
                return (index - prevPartitionIndex - 1) * max_val
            if(index == len(arr) or (index - prevPartitionIndex) > k):
                return -float("Inf")
            if((index, prevPartitionIndex) in mem):
                return mem[(index, prevPartitionIndex)]
            max_sum = makeMaxSum(index + 1, prevPartitionIndex, max(arr[index], max_val))
            mem[(index, prevPartitionIndex)] =  max(max_sum, (index - prevPartitionIndex) * max(max_val, arr[index]) + makeMaxSum(index + 1, index, 0))
            return mem[(index, prevPartitionIndex)]
        return makeMaxSum(0, -1, 0)

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp  = [1] * (len(arr) + 1)
        dp[0] = 0
        for i in range(1, len(arr) + 1):
            max_val = arr[i - 1]
            for j in range(i, max(i - k, 0), -1):
                max_val = max(max_val, arr[j - 1])
                dp[i] =  max(dp[i], max_val * (i - j + 1) + dp[j - 1])
        return dp[len(arr)]

            

