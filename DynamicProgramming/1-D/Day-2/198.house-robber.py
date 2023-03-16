#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Medium (45.54%)
# Total Accepted:    1.5M
# Total Submissions: 3M
# Testcase Example:  '[1,2,3,1]'
#
# <p>You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and <b>it will automatically contact the police if two adjacent
# houses were broken into on the same night</b>.</p>
# 
# <p>Given an integer array <code>nums</code> representing the amount of money
# of each house, return <em>the maximum amount of money you can rob tonight
# <b>without alerting the police</b></em>.</p>
# 
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# 
# <pre>
# <strong>Input:</strong> nums = [1,2,3,1]
# <strong>Output:</strong> 4
# <strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3
# (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# </pre>
# 
# <p><strong class="example">Example 2:</strong></p>
# 
# <pre>
# <strong>Input:</strong> nums = [2,7,9,3,1]
# <strong>Output:</strong> 12
# <strong>Explanation:</strong> Rob house 1 (money = 2), rob house 3 (money =
# 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# </pre>
# 
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# 
# <ul>
# <li><code>1 &lt;= nums.length &lt;= 100</code></li>
# <li><code>0 &lt;= nums[i] &lt;= 400</code></li>
# </ul>
# 
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        def traverse(index):
            if(index >= len(nums)):
                return 0
            if(index in mem):
                return mem[index]
            mem[index] = max(nums[index] + traverse(index + 2), traverse(index + 1))
            return mem[index]

        return traverse(0)
    
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[0], dp[1] = 0, nums[0]
        for i in range(1, len(nums)):
            dp[i + 1] =  max(nums[i] + dp[i - 1], dp[i])
        return dp[len(nums)]
        
