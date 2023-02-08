#
# @lc app=leetcode id=1028 lang=python
#
# [1028] Recover a Tree From Preorder Traversal
#
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/
#
# algorithms
# Hard (73.15%)
# Likes:    1357
# Dislikes: 37
# Total Accepted:    41.2K
# Total Submissions: 56.4K
# Testcase Example:  '"1-2--3--4-5--6--7"'
#
# We run a preorder depth-first search (DFS) on the root of a binary tree.
# 
# At each node in this traversal, we output D dashes (where D is the depth of
# this node), then we output the value of this node.  If the depth of a node is
# D, the depth of its immediate child is D + 1.  The depth of the root node is
# 0.
# 
# If a node has only one child, that child is guaranteed to be the left child.
# 
# Given the output traversal of this traversal, recover the tree and return its
# root.
# 
# 
# Example 1:
# 
# 
# Input: traversal = "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
# 
# 
# Example 2:
# 
# 
# Input: traversal = "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
# 
# 
# Example 3:
# 
# 
# Input: traversal = "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the original tree is in the range [1, 1000].
# 1 <= Node.val <= 10^9
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack, index = [], 0
        while(index < len(traversal)):
            dashes, val = 0, ''
            while(index < len(traversal) and traversal[index] == '-'):
                index, dashes = index + 1, dashes + 1
            while(index < len(traversal) and traversal[index].isnumeric()):
                index, val = index + 1, val + traversal[index]
            while(len(stack) > dashes):
                stack.pop()
            node = TreeNode(val)
            if(stack and not stack[-1].left):
                stack[-1].left = node
            elif(stack):
                stack[-1].right = node
            stack.append(node)
        return stack[0]

    def recursiveApproach(self, traversal):
        if(not traversal):
            return None
        self.head = None
        self.index = 0
        def construct(depth):
            if(self.index == len(traversal)):
                return None
            num, dashes, i = 0, 0, self.index
            while(i < len(traversal)):
                if(traversal[i] == '-'):
                    dashes += 1
                else:
                    break
                i += 1
            if(dashes != depth):
                return None
            while(i < len(traversal)):
                if(traversal[i].isnumeric()):
                    num = num * 10 + int(traversal[i])
                else:
                    break
                i += 1
            root = TreeNode(num)
            self.index = i
            root.left = construct(depth + 1)
            root.right = construct(depth + 1)
            return root
        return construct(0)


        
# @lc code=end

