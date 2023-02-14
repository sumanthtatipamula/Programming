#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (60.04%)
# Total Accepted:    529.2K
# Total Submissions: 878.4K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
# 
# According to Wikipedia, every level, except possibly the last, is completely
# filled in a complete binary tree, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2^h nodes inclusive at the last
# level h.
# 
# Design an algorithm that runs in less than O(n) time complexity.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5,6]
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def extremeHeight(root, left):
            count = 0
            while(root):
                count += 1
                root = root.left if(left) else root.right
            return count
        def traverse(root):
            if(not root):
                return 0
            left = extremeHeight(root.left, True)
            right = extremeHeight(root.right, False)
            if(left == right):
                return 2 ** (left + 1) - 1
            return 1 + traverse(root.left) + traverse(root.right)
        return traverse(root)
        
