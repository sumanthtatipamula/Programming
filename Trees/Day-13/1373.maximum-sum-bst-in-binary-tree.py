#
# @lc app=leetcode id=1373 lang=python3
#
# [1373] Maximum Sum BST in Binary Tree
#
# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/description/
#
# algorithms
# Hard (39.31%)
# Total Accepted:    48K
# Total Submissions: 121.9K
# Testcase Example:  '[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]'
#
# Given a binary tree root, return the maximum sum of all keys of any sub-tree
# which is also a Binary Search Tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# Output: 20
# Explanation: Maximum sum in a valid Binary search tree is obtained in root
# node with key equal to 3.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [4,3,null,1,2]
# Output: 2
# Explanation: Maximum sum in a valid Binary search tree is obtained in a
# single root node with key equal to 2.
# 
# 
# Example 3:
# 
# 
# Input: root = [-4,-2,-5]
# Output: 0
# Explanation: All values are negatives. Return an empty BST.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 4 * 10^4].
# -4 * 10^4 <= Node.val <= 4 * 10^4
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
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def traverse(root):
            if(not root):
                return [float("Inf"), -float("Inf"), 0] # min, max, sum
            left = traverse(root.left)
            right = traverse(root.right)
            if(root.val > left[1] and root.val < right[0]):
                self.result = max(self.result, left[-1]+ right[-1] + root.val)
                return [min(root.val,left[0]),max(root.val,right[1]),left[-1]+ right[-1] + root.val]
            return [-float("Inf"), float("Inf"), max(left[-1], right[-1])]
        traverse(root)
        return self.result
        
