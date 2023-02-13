#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#
# https://leetcode.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (64.61%)
# Total Accepted:    123.7K
# Total Submissions: 191K
# Testcase Example:  '[5,2,-3]'
#
# Given the root of a binary tree, return the most frequent subtree sum. If
# there is a tie, return all the values with the highest frequency in any
# order.
# 
# The subtree sum of a node is defined as the sum of all the node values formed
# by the subtree rooted at that node (including the node itself).
# 
# 
# Example 1:
# 
# 
# Input: root = [5,2,-3]
# Output: [2,-3,4]
# 
# 
# Example 2:
# 
# 
# Input: root = [5,2,-5]
# Output: [2]
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freqmap = defaultdict(int)
        self.max_freq = 0
        def traverse(root):
            if(not root):
                return 0
            total = root.val + traverse(root.left) + traverse(root.right)
            freqmap[total] += 1
            self.max_freq = max(self.max_freq, freqmap[total])
            return total
        traverse(root)
        result = []
        for k,v in freqmap.items():
            if(v == self.max_freq):
                result.append(k)
        return result
