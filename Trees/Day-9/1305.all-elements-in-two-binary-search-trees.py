#
# @lc app=leetcode id=1305 lang=python
#
# [1305] All Elements in Two Binary Search Trees
#
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/
#
# algorithms
# Medium (79.81%)
# Likes:    2669
# Dislikes: 78
# Total Accepted:    184.1K
# Total Submissions: 230.5K
# Testcase Example:  '[2,1,4]\n[1,0,3]'
#
# Given two binary search trees root1 and root2, return a list containing all
# the integers from both trees sorted in ascending order.
# 
# 
# Example 1:
# 
# 
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each tree is in the range [0, 5000].
# -10^5 <= Node.val <= 10^5
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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1, list2, result, i,j = [],[], [], 0,0
        def inorder(root, list_of_elements):
            if(not root):
                return 
            inorder(root.left, list_of_elements)
            list_of_elements.append(root.val)
            inorder(root.right, list_of_elements)
        inorder(root1,list1)
        inorder(root2, list2)
        while(i < len(list1) and j < len(list2)):
            if(list1[i] < list2[j]):
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        result += list1[i:] if(i < len(list1)) else list2[j:]
        return result
        
        
# @lc code=end

