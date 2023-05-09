#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.74%)
# Total Accepted:    515K
# Total Submissions: 1.1M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# <p>Given an unsorted array of integers <code>nums</code>, return <em>the
# length of the longest consecutive elements sequence.</em></p>
# 
# <p>You must write an algorithm that runs
# in&nbsp;<code>O(n)</code>&nbsp;time.</p>
# 
# <p>&nbsp;</p>
# <p><strong>Example 1:</strong></p>
# 
# <pre>
# <strong>Input:</strong> nums = [100,4,200,1,3,2]
# <strong>Output:</strong> 4
# <strong>Explanation:</strong> The longest consecutive elements sequence is
# <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
# </pre>
# 
# <p><strong>Example 2:</strong></p>
# 
# <pre>
# <strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
# <strong>Output:</strong> 9
# </pre>
# 
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# 
# <ul>
# <li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
# <li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
# </ul>
# 
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
