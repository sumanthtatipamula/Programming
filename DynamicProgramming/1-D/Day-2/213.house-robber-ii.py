#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (38.98%)
# Total Accepted:    527.9K
# Total Submissions: 1.3M
# Testcase Example:  '[2,3,2]'
#
# <p>You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# <strong>arranged in a circle.</strong> That means the first house is the
# neighbor of the last one. Meanwhile, adjacent houses have a security system
# connected, and&nbsp;<b>it will automatically contact the police if two
# adjacent houses were broken into on the same night</b>.</p>
# 
# <p>Given an integer array <code>nums</code> representing the amount of money
# of each house, return <em>the maximum amount of money you can rob tonight
# <strong>without alerting the police</strong></em>.</p>
# 
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# 
# <pre>
# <strong>Input:</strong> nums = [2,3,2]
# <strong>Output:</strong> 3
# <strong>Explanation:</strong> You cannot rob house 1 (money = 2) and then rob
# house 3 (money = 2), because they are adjacent houses.
# </pre>
# 
# <p><strong class="example">Example 2:</strong></p>
# 
# <pre>
# <strong>Input:</strong> nums = [1,2,3,1]
# <strong>Output:</strong> 4
# <strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3
# (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# </pre>
# 
# <p><strong class="example">Example 3:</strong></p>
# 
# <pre>
# <strong>Input:</strong> nums = [1,2,3]
# <strong>Output:</strong> 3
# </pre>
# 
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# 
# <ul>
# <li><code>1 &lt;= nums.length &lt;= 100</code></li>
# <li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
# </ul>
# 
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        if(len(nums) == 1):
            return nums[0]
        def traverse(index, end):
            if(index >= end):
                return 0
            if(index in mem):
                return mem[index]
            mem[index] = max(nums[index] + traverse(index + 2, end), traverse(index + 1, end))
            return mem[index]

        result1 = traverse(0, len(nums) - 1)
        mem= {}
        result2 =  traverse(1, len(nums))
        return max(result1, result2)
        
