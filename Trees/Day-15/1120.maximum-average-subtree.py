#
# @lc app=leetcode id=1120 lang=python3
#
# [1120] Maximum Average Subtree
#
# https://leetcode.com/problems/maximum-average-subtree/description/
#
# algorithms
# Medium (65.53%)
# Total Accepted:    58.7K
# Total Submissions: 89.6K
# Testcase Example:  '[5,6,1]'
#
# Given the root of a binary tree, return the maximum average value of a
# subtree of that tree. Answers within 10^-5 of the actual answer will be
# accepted.
# 
# A subtree of a tree is any node of that tree plus all its descendants.
# 
# The average value of a tree is the sum of its values, divided by the number
# of nodes.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,6,1]
# Output: 6.00000
# Explanation: 
# For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
# For the node with value = 6 we have an average of 6 / 1 = 6.
# For the node with value = 1 we have an average of 1 / 1 = 1.
# So the answer is 6 which is the maximum.
# 
# 
# Example 2:
# 
# 
# Input: root = [0,null,1]
# Output: 1.00000
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^5
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
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_average = -float("Inf")
        def traverse(root):
            if(not root):
                return [0, 0]
            left = traverse(root.left)
            right = traverse(root.right)
            total, elements = left[0] + right[0] + root.val, left[1] + right[1] + 1
            if(elements):
                self.max_average = max(self.max_average, total / elements)
            return [total, elements]
        traverse(root)
        return self.max_average
        
