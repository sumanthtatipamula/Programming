#
# @lc app=leetcode id=1026 lang=python
#
# [1026] Maximum Difference Between Node and Ancestor
#
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
#
# algorithms
# Medium (75.79%)
# Likes:    3851
# Dislikes: 93
# Total Accepted:    196.6K
# Total Submissions: 259.4K
# Testcase Example:  '[8,3,10,1,6,null,14,null,null,4,7,13]'
#
# Given the root of a binary tree, find the maximum value v for which there
# exist different nodes a and b where v = |a.val - b.val| and a is an ancestor
# of b.
# 
# A node a is an ancestor of b if either: any child of a is equal to b or any
# child of a is an ancestor of b.
# 
# 
# Example 1:
# 
# 
# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are
# given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1|
# = 7.
# 
# Example 2:
# 
# 
# Input: root = [1,null,2,null,0,3]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 5000].
# 0 <= Node.val <= 10^5
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def findMaxDiff(root, min_val, max_val):
            if(not root):
                return max_val - min_val
            min_val = min(root.val, min_val)
            max_val = max(root.val, max_val)
            return max(findMaxDiff(root.right, min_val,max_val),findMaxDiff(root.left,min_val,max_val))
        return findMaxDiff(root, root.val, root.val)
        
# @lc code=end

