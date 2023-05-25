#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#
# https://leetcode.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (80.00%)
# Total Accepted:    108.7K
# Total Submissions: 136K
# Testcase Example:  '7'
#
# Given an integer n, return a list of all possible full binary trees with n
# nodes. Each node of each tree in the answer must have Node.val == 0.
# 
# Each element of the answer is the root node of one possible tree. You may
# return the final list of trees in any order.
# 
# A full binary tree is a binary tree where each node has exactly 0 or 2
# children.
# 
# 
# Example 1:
# 
# 
# Input: n = 7
# Output:
# [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: [[0,0,0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
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
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if(n % 2 == 0):
            return []
        dp = [[] for _ in range(n + 1)]
        dp[1] = [TreeNode(0)]
        for k in range(3, n + 1, 2):
            for i in range(1, k - 1, 2):
                for left_sub_tree in dp[i]:
                    for right_sub_tree in dp[k - i - 1]:
                        root = TreeNode(0)
                        root.left = left_sub_tree
                        root.right = right_sub_tree
                        dp[k].append(root)
        return dp[n]
        
