#
# @lc app=leetcode id=298 lang=python3
#
# [298] Binary Tree Longest Consecutive Sequence
#
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/
#
# algorithms
# Medium (52.63%)
# Total Accepted:    136.5K
# Total Submissions: 259K
# Testcase Example:  '[1,null,3,2,4,null,null,null,5]'
#
# Given the root of a binary tree, return the length of the longest consecutive
# sequence path.
# 
# A consecutive sequence path is a path where the values increase by one along
# the path.
# 
# Note that the path can start at any node in the tree, and you cannot go from
# a node to its parent in the path.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,3,2,4,null,null,null,5]
# Output: 3
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [2,null,3,2,null,1]
# Output: 2
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return
# 2.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -3 * 10^4 <= Node.val <= 3 * 10^4
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.result = 1
        def traverse(root, parentVal, count):
            if(not root):
                return 0
            if(root.val == parentVal + 1):
                count += 1
                self.result = max(self.result, count)
            else:
                count = 1
            traverse(root.left, root.val, count)
            traverse(root.right, root.val, count)
        traverse(root, -1, 1)
        return self.result
        
