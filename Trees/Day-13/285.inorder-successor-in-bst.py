#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#
# https://leetcode.com/problems/inorder-successor-in-bst/description/
#
# algorithms
# Medium (48.54%)
# Total Accepted:    298K
# Total Submissions: 612.9K
# Testcase Example:  '[2,1,3]\n1'
#
# Given the root of a binary search tree and a node p in it, return the
# in-order successor of that node in the BST. If the given node has no in-order
# successor in the tree, return null.
# 
# The successor of a node p is the node with the smallest key greater than
# p.val.
# 
# 
# Example 1:
# 
# 
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the
# return value is of TreeNode type.
# 
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the
# answer is null.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5
# All Nodes will have unique values.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        succ = None
        while(root):
            if(root.val > p.val):
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

        # comments solution must be executed
        # def recursive(root, parent):
        #     if(not root):
        #         return None
        #     if(root.val > p.val):
        #         return traverse(root.left, root)
        #     elif(root.val < p.val):
        #         return traverse(root.right, parent)
        #     else:
        #         successor = None
        #         root = root.right
        #         while(root):
        #             successor = root
        #             root = root.left
        #         return parent if(not successor) else successor
        # return recursive(root, None)
        
