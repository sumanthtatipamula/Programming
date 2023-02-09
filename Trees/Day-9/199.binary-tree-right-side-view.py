#
# @lc app=leetcode id=199 lang=python
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (57.73%)
# Likes:    4965
# Dislikes: 270
# Total Accepted:    528.6K
# Total Submissions: 911.6K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# 
# 
# Example 2:
# 
# 
# Input: root = [1,null,3]
# Output: [1,3]
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
#

# @lc code=start
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(root, curr_level):
            if(not root):
                return
            if(curr_level >= len(result)):
                result.append(root.val)
            traverse(root.right, curr_level + 1)
            traverse(root.left, curr_level + 1)
        traverse(root, 0)
        return result
        
# @lc code=end

