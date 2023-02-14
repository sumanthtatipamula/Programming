#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#
# https://leetcode.com/problems/deepest-leaves-sum/description/
#
# algorithms
# Medium (86.79%)
# Total Accepted:    263.6K
# Total Submissions: 303.9K
# Testcase Example:  '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
#
# Given the root of a binary tree, return the sum of values of its deepest
# leaves.
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# 
# 
# Example 2:
# 
# 
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# 1 <= Node.val <= 100
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.max_level = 0
        self.leaf_sum = 0
        def traverse(root, level):
            if(not root):
                return 0
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)    
            if(not root.left and not root.right):
                if(level >= self.max_level):
                    self.leaf_sum = root.val if(level > self.max_level) else self.leaf_sum + root.val
                    self.max_level = level
        traverse(root, 1)
        return self.leaf_sum
        
