#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (63.54%)
# Likes:    4892
# Dislikes: 309
# Total Accepted:    621K
# Total Submissions: 974.4K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
# 
# A height-balanced binary tree is a binary tree in which the depth of the two
# subtrees of every node never differs by more than one.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(start, end):
            if(start > end):
                return None
            mid = start + (end - start) // 2
            root = TreeNode(nums[mid])
            root.left = construct(start, mid - 1)
            root.right = construct(mid + 1, end)
            return root
        return construct(0, len(nums) - 1)
        
# @lc code=end

