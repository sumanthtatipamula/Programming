#
# @lc app=leetcode id=250 lang=python3
#
# [250] Count Univalue Subtrees
#
# https://leetcode.com/problems/count-univalue-subtrees/description/
#
# algorithms
# Medium (55.33%)
# Total Accepted:    136.1K
# Total Submissions: 245.8K
# Testcase Example:  '[5,1,5,5,5,null,5]'
#
# Given the root of a binary tree, return the number of uni-value subtrees.
# 
# A uni-value subtree means all nodes of the subtree have the same value.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,1,5,5,5,null,5]
# Output: 4
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
# Input: root = [5,5,5,5,5,null,5]
# Output: 6
# 
# 
# 
# Constraints:
# 
# 
# The number of the node in the tree will be in the range [0, 1000].
# -1000 <= Node.val <= 1000
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
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def traverse(root, val):
            if(not root):
                return True
            if(not traverse(root.left, root.val) or not traverse(root.right, root.val)):
                return False
            self.result += 1
            return True
        traverse(root, 0)
        return self.result

        
