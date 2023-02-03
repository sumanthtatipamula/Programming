#
# @lc app=leetcode id=687 lang=python
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Medium (40.24%)
# Likes:    3725
# Dislikes: 643
# Total Accepted:    159.7K
# Total Submissions: 395.8K
# Testcase Example:  '[5,4,5,1,1,null,5]'
#
# Given the root of a binary tree, return the length of the longest path, where
# each node in the path has the same value. This path may or may not pass
# through the root.
# 
# The length of the path between two nodes is represented by the number of
# edges between them.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,4,5,1,1,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value
# (i.e. 5).
# 
# 
# Example 2:
# 
# 
# Input: root = [1,4,5,4,4,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value
# (i.e. 4).
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_value = 1
        def traverse(root):
            if(not root):
                return 0
            left_count = traverse(root.left)
            right_count = traverse(root.right)
            left, right = 0,0 
            if(left_count > 0 and root.left.val == root.val):
                left = left_count
            if(right_count > 0 and root.right.val == root.val):
                right = right_count
            self.max_value = max(self.max_value, left + right + 1)
            return max(left, right) + 1
        traverse(root)
        return self.max_value - 1
        
# @lc code=end

