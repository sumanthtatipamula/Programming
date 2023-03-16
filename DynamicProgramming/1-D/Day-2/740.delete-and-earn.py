#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#
# https://leetcode.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (53.91%)
# Total Accepted:    247.6K
# Total Submissions: 432.4K
# Testcase Example:  '[3,4,2]'
#
# <p>You are given an integer array <code>nums</code>. You want to maximize the
# number of points you get by performing the following operation any number of
# times:</p>
# 
# <ul>
# <li>Pick any <code>nums[i]</code> and delete it to earn <code>nums[i]</code>
# points. Afterwards, you must delete <b>every</b> element equal to
# <code>nums[i] - 1</code> and <strong>every</strong> element equal to
# <code>nums[i] + 1</code>.</li>
# </ul>
# 
# <p>Return <em>the <strong>maximum number of points</strong> you can earn by
# applying the above operation some number of times</em>.</p>
# 
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# 
# <pre>
# <strong>Input:</strong> nums = [3,4,2]
# <strong>Output:</strong> 6
# <strong>Explanation:</strong> You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# </pre>
# 
# <p><strong class="example">Example 2:</strong></p>
# 
# <pre>
# <strong>Input:</strong> nums = [2,2,3,3,3,4]
# <strong>Output:</strong> 9
# <strong>Explanation:</strong> You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2&#39;s and 4&#39;s are also deleted. nums
# = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.</pre>
# 
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# 
# <ul>
# <li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
# <li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
# </ul>
# 
#
class Solution:
    # Top Down Approach
    def deleteAndEarn(self, nums: List[int]) -> int:
        new_nums = []
        freq = {}
        mem = {}
        for num in nums:
            if(num not in freq):
                freq[num] = 0
                new_nums.append(num)
            freq[num] += num
        new_nums.sort()
        def traverse(index):
            if(index == len(new_nums)):
                return 0
            if(index in mem):
                return mem[index]
            next_index = index + 1
            if(index < len(new_nums) - 1 and new_nums[index + 1] == new_nums[index] + 1):
                next_index = index + 2
            mem[index] = max(freq[new_nums[index]] + traverse(next_index), traverse(index + 1))
            return mem[index]
        return traverse(0)
    
    # Bottom Up Approach
    def deleteAndEarn(self, nums: List[int]) -> int:
        new_nums = []
        freq = {}
        for num in nums:
            if(num not in freq):
                freq[num] = 0
                new_nums.append(num)
            freq[num] += num
        new_nums.sort()
        dp = [0] * (len(new_nums) + 1)
        dp[0] = 0
        dp[1] = freq[new_nums[0]]
        for i in range(1, len(new_nums)):
            if(new_nums[i] != new_nums[i - 1] + 1):
                dp[i + 1] = freq[new_nums[i]] + dp[i]
            else:
                dp[i + 1] = max(freq[new_nums[i]] + dp[i - 1], dp[i])
        return dp[len(new_nums)]
    
    # Optimised Bottom Up Approach
    def deleteAndEarn(self, nums: List[int]) -> int:
        new_nums = []
        freq = {}
        for num in nums:
            if(num not in freq):
                freq[num] = 0
                new_nums.append(num)
            freq[num] += num
        new_nums.sort()
        pprev = 0
        prev = freq[new_nums[0]]
        for i in range(1, len(new_nums)):
            curr = 0
            if(new_nums[i] != new_nums[i - 1] + 1):
                curr = freq[new_nums[i]] + prev
            else:
                curr = max(freq[new_nums[i]] + pprev, prev)
            pprev = prev
            prev = curr
        return prev
            
