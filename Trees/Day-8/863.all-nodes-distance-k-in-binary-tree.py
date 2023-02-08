#
# @lc app=leetcode id=863 lang=python
#
# [863] All Nodes Distance K in Binary Tree
#
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (62.21%)
# Likes:    8034
# Dislikes: 159
# Total Accepted:    291.9K
# Total Submissions: 468.9K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# Given the root of a binary tree, the value of a target node target, and an
# integer k, return an array of the values of all nodes that have a distance k
# from the target node.
# 
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value
# 5) have values 7, 4, and 1.
# 
# 
# Example 2:
# 
# 
# Input: root = [1], target = 1, k = 3
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 500].
# 0 <= Node.val <= 500
# All the values Node.val are unique.
# target is the value of one of the nodes in the tree.
# 0 <= k <= 1000
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.result = []
        if(k == 0):
            return [target.val]
        def addNodesAtDistanceK(root, distance):
            if(not root or distance > k):
                return 
            if(distance + 1 == k):
                self.result.append(root.val)
            addNodesAtDistanceK(root.left, distance + 1)
            addNodesAtDistanceK(root.right, distance + 1)
        def traverse(root):
            if(not root):
                return 0
            if(root.val == target.val):
                addNodesAtDistanceK(root.left, 0)
                addNodesAtDistanceK(root.right, 0)
                return 1
            inLeftSubTree = traverse(root.left)
            if(inLeftSubTree == k):
                self.result.append(root.val)
            if(inLeftSubTree > 0 and inLeftSubTree < k):
                addNodesAtDistanceK(root.right, inLeftSubTree)
                return inLeftSubTree + 1
            inRightSubTree = traverse(root.right)
            if(inRightSubTree == k):
                self.result.append(root.val)
            if(inRightSubTree > 0 and inRightSubTree < k):
                addNodesAtDistanceK(root.left, inRightSubTree)
                return inRightSubTree + 1
            return 0
        traverse(root)
        return self.result
# @lc code=end

