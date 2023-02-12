#
# @lc app=leetcode id=333 lang=python3
#
# [333] Largest BST Subtree
#
# https://leetcode.com/problems/largest-bst-subtree/description/
#
# algorithms
# Medium (42.64%)
# Total Accepted:    94.7K
# Total Submissions: 221.7K
# Testcase Example:  '[10,5,15,1,8,null,7]'
#
# Given the root of a binary tree, find the largest subtree, which is also a
# Binary Search Tree (BST), where the largest means subtree has the largest
# number of nodes.
# 
# A Binary Search Tree (BST) is a tree in which all the nodes follow the
# below-mentioned properties:
# 
# 
# The left subtree values are less than the value of their parent (root) node's
# value.
# The right subtree values are greater than the value of their parent (root)
# node's value.
# 
# 
# Note: A subtree must include all of its descendants.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [10,5,15,1,8,null,7]
# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted one. The
# return value is the subtree's size, which is 3.
# 
# Example 2:
# 
# 
# Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -10^4 <= Node.val <= 10^4
# 
# 
# 
# Follow up: Can you figure out ways to solve it with O(n) time complexity?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if(not root):
                return [float("Inf"), -float("Inf"), 0] # min, max, count
            left = traverse(root.left)
            right = traverse(root.right)
            if(root.val > left[1] and root.val < right[0]):
                return [min(root.val,left[0]), max(root.val,right[1]), left[-1] + right[-1] + 1]
            return [-float("Inf"), float("Inf"), max(left[-1], right[-1])]
        return traverse(root)[-1]
        
