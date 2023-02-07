#
# @lc app=leetcode id=2385 lang=python
#
# [2385] Amount of Time for Binary Tree to Be Infected
#
# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/
#
# algorithms
# Medium (56.28%)
# Likes:    853
# Dislikes: 12
# Total Accepted:    21.5K
# Total Submissions: 38.1K
# Testcase Example:  '[1,5,3,null,4,10,6,9,2]\n3'
#
# You are given the root of a binary tree with unique values, and an integer
# start. At minute 0, an infection starts from the node with value start.
# 
# Each minute, a node becomes infected if:
# 
# 
# The node is currently uninfected.
# The node is adjacent to an infected node.
# 
# 
# Return the number of minutes needed for the entire tree to be infected.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,5,3,null,4,10,6,9,2], start = 3
# Output: 4
# Explanation: The following nodes are infected during:
# - Minute 0: Node 3
# - Minute 1: Nodes 1, 10 and 6
# - Minute 2: Node 5
# - Minute 3: Node 4
# - Minute 4: Nodes 9 and 2
# It takes 4 minutes for the whole tree to be infected so we return 4.
# 
# 
# Example 2:
# 
# 
# Input: root = [1], start = 1
# Output: 0
# Explanation: At minute 0, the only node in the tree is infected so we return
# 0.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^5].
# 1 <= Node.val <= 10^5
# Each node has a unique value.
# A node with a value of start exists in the tree.
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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.max_time = 0
        def infect(root):
            if(not root):
                return 0
            root.val = -1
            return 1 + max(infect(root.left), infect(root.right))
        def traverse(root):
            if(not root or root.val == -1):
                return 0
            if(root.val == start):
                left = infect(root.left)
                right = infect(root.right)
                self.max_time = max(left,right)
                root.val = -1
                return 1
            inLeftSubTree = traverse(root.left)
            if(inLeftSubTree):
                self.max_time = max(self.max_time,inLeftSubTree + infect(root.right))
                return inLeftSubTree + 1
            inRightSubTree = traverse(root.right)
            if(inRightSubTree):
                self.max_time = max(self.max_time,inRightSubTree + infect(root.left))
                return inRightSubTree + 1
            return 0
        traverse(root)
        return self.max_time
# @lc code=end

