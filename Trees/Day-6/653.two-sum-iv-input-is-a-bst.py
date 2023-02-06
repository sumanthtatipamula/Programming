#
# @lc app=leetcode id=653 lang=python
#
# [653] Two Sum IV - Input is a BST
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (61.01%)
# Likes:    5569
# Dislikes: 236
# Total Accepted:    437.2K
# Total Submissions: 716.4K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# Given the root of a binary search tree and an integer k, return true if there
# exist two elements in the BST such that their sum is equal to k, or false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -10^4 <= Node.val <= 10^4
# root is guaranteed to be a valid binary search tree.
# -10^5 <= k <= 10^5
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        mp = set()
        self.found = False
        def traverse(root):
            if(not root):
                return None
            traverse(root.left)
            if((k - root.val) in mp):
                self.found = True
                return
            mp.add(root.val)
            traverse(root.right)
        traverse(root)
        return self.found
        
# @lc code=end

