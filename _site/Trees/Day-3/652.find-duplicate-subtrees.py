#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (56.51%)
# Total Accepted:    180.3K
# Total Submissions: 318.9K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given the root of a binary tree, return all duplicate subtrees.
# 
# For each kind of duplicate subtrees, you only need to return the root node of
# any one of them.
# 
# Two trees are duplicate if they have the same structure with the same node
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# 
# 
# Example 2:
# 
# 
# Input: root = [2,1,1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# 
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the tree will be in the range [1, 5000]
# -200 <= Node.val <= 200
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
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        serialIdToCount = {}
        result = []
        def traverse(root):
            if(not root):
                return '#'
            left_serial_id = traverse(root.left)
            right_serial_id = traverse(root.right)
            serial_id = str(root.val) + ',' + left_serial_id + ',' + right_serial_id
            if(serial_id in serialIdToCount):
                serialIdToCount[serial_id] += 1
            else:
                serialIdToCount[serial_id] = 1
            if(serialIdToCount[serial_id] == 2):
                result.append(root)
            return serial_id
        traverse(root)
        return result
        
