#
# @lc app=leetcode id=1740 lang=python3
#
# [1740] Find Distance in a Binary Tree
#
# https://leetcode.com/problems/find-distance-in-a-binary-tree/description/
#
# algorithms
# Medium (68.87%)
# Total Accepted:    17.7K
# Total Submissions: 25.7K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n0'
#
# Given the root of a binary tree and two integers p and q, return the distance
# between the nodes of value p and value q in the tree.
# 
# The distance between two nodes is the number of edges on the path from one to
# the other.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
# Output: 3
# Explanation: There are 3 edges between 5 and 0: 5-3-1-0.
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7
# Output: 2
# Explanation: There are 2 edges between 5 and 7: 5-2-7.
# 
# Example 3:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5
# Output: 0
# Explanation: The distance between a node and itself is 0.
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^9
# All Node.val are unique.
# p and q are values in the tree.
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
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        self.result = 0
        def traverse(root):
            if(not root):
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            if(left and right):
                self.result = left + right
            if(root.val == p or root.val == q):
                if(left or right):
                    self.result = left or right
                    return 0
                return 1
            return (left or right) + 1 if(left or right) else 0
        traverse(root)
        return self.result
        
        
