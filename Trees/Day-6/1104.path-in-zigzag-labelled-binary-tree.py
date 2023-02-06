#
# @lc app=leetcode id=1104 lang=python
#
# [1104] Path In Zigzag Labelled Binary Tree
#
# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/description/
#
# algorithms
# Medium (75.01%)
# Likes:    1261
# Dislikes: 292
# Total Accepted:    38.4K
# Total Submissions: 51.1K
# Testcase Example:  '14'
#
# In an infinite binary tree where every node has two children, the nodes are
# labelled in row order.
# 
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is
# left to right, while in the even numbered rows (second, fourth, sixth,...),
# the labelling is right to left.
# 
# 
# 
# Given the label of a node in this tree, return the labels in the path from
# the root of the tree to the node with that label.
# 
# 
# Example 1:
# 
# 
# Input: label = 14
# Output: [1,3,4,14]
# 
# 
# Example 2:
# 
# 
# Input: label = 26
# Output: [1,2,6,10,26]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= label <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        result = []
        if(label == 1):
            return [1]
        level = 0
        n = label
        while(n != 0):
            level += 1
            n >>= 1
        result.append(label)
        while(label != 1):
            levelMax = (2 ** level ) - 1
            levelMin = 2 ** (level - 1)
            label = abs(levelMax + levelMin - label) // 2
            level -= 1
            result.append(label)
        return result[::-1]
        
# @lc code=end

