#
# @lc app=leetcode id=501 lang=python
#
# [501] Find Mode in Binary Search Tree
#
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (45.30%)
# Likes:    1669
# Dislikes: 473
# Total Accepted:    125.9K
# Total Submissions: 276.9K
# Testcase Example:  '[1,null,2,2]'
#
# Given the root of a binary search tree (BST) with duplicates, return all the
# mode(s) (i.e., the most frequently occurred element) in it.
# 
# If the tree has more than one mode, return them in any order.
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
# The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,2]
# Output: [2]
# 
# 
# Example 2:
# 
# 
# Input: root = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5
# 
# 
# 
# Follow up: Could you do that without using any extra space? (Assume that the
# implicit stack space incurred due to recursion does not count).
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.current_count, self.max_count = 0,0
        self.prev, self.result = None, []
        def traverse(root):
            if(not root):
                return
            traverse(root.left)
            if(self.prev == root.val):
                self.current_count += 1
            else:
                self.current_count = 1
                self.prev = root.val
            if(self.current_count > self.max_count):
                self.result = [root.val]
                self.max_count = self.current_count
            elif(self.current_count == self.max_count):
                self.result.append(root.val)
            traverse(root.right)
        traverse(root)
        return self.result
        
# @lc code=end

