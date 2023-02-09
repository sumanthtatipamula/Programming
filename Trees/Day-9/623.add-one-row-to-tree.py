#
# @lc app=leetcode id=623 lang=python
#
# [623] Add One Row to Tree
#
# https://leetcode.com/problems/add-one-row-to-tree/description/
#
# algorithms
# Medium (59.47%)
# Likes:    2682
# Dislikes: 224
# Total Accepted:    147.3K
# Total Submissions: 247.7K
# Testcase Example:  '[4,2,6,3,1,5]\n1\n2'
#
# Given the root of a binary tree and two integers val and depth, add a row of
# nodes with value val at the given depth depth.
# 
# Note that the root node is at depth 1.
# 
# The adding rule is:
# 
# 
# Given the integer depth, for each not null tree node cur at the depth depth -
# 1, create two tree nodes with value val as cur's left subtree root and right
# subtree root.
# cur's original left subtree should be the left subtree of the new left
# subtree root.
# cur's original right subtree should be the right subtree of the new right
# subtree root.
# If depth == 1 that means there is no depth depth - 1 at all, then create a
# tree node with value val as the new root of the whole original tree, and the
# original tree is the new root's left subtree.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [4,2,6,3,1,5], val = 1, depth = 2
# Output: [4,1,1,2,null,null,6,3,1,5]
# 
# 
# Example 2:
# 
# 
# Input: root = [4,2,null,3,1], val = 1, depth = 3
# Output: [4,2,null,1,1,3,null,null,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# The depth of the tree is in the range [1, 10^4].
# -100 <= Node.val <= 100
# -10^5 <= val <= 10^5
# 1 <= depth <= the depth of tree + 1
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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if(depth == 1):
            new_root = TreeNode(val)
            new_root.left =  root
            return new_root
        queue = deque([root])
        depth -= 1
        while(depth):
            if(depth > 1):
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if(node.left):
                        queue.append(node.left)
                    if(node.right):
                        queue.append(node.right)
            if(depth == 1):
                for node in queue:
                    left_new_node, right_new_node = TreeNode(val), TreeNode(val)
                    node.left, left_new_node.left = left_new_node, node.left or None
                    node.right, right_new_node.right = right_new_node, node.right or None
            depth -= 1
        return root
        
# @lc code=end

