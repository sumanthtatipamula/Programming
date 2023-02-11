#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (39.47%)
# Total Accepted:    127.3K
# Total Submissions: 321.9K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# <p>Given the <code>root</code> of a binary tree, return <em>the
# <strong>maximum width</strong> of the given tree</em>.</p>
# 
# <p>The <strong>maximum width</strong> of a tree is the maximum
# <strong>width</strong> among all levels.</p>
# 
# <p>The <strong>width</strong> of one level is defined as the length between
# the end-nodes (the leftmost and rightmost non-null nodes), where the null
# nodes between the end-nodes are also counted into the length
# calculation.</p>
# 
# <p>It is <strong>guaranteed</strong> that the answer will in the range of
# <strong>32-bit</strong> signed integer.</p>
# 
# <p>&nbsp;</p>
# <p><strong>Example 1:</strong></p>
# <img alt=""
# src="https://assets.leetcode.com/uploads/2021/05/03/width1-tree.jpg"
# style="width: 359px; height: 302px;" />
# <pre>
# <strong>Input:</strong> root = [1,3,2,5,3,null,9]
# <strong>Output:</strong> 4
# <strong>Explanation:</strong> The maximum width existing in the third level
# with the length 4 (5,3,null,9).
# </pre>
# 
# <p><strong>Example 2:</strong></p>
# <img alt=""
# src="https://assets.leetcode.com/uploads/2021/05/03/width2-tree.jpg"
# style="width: 224px; height: 302px;" />
# <pre>
# <strong>Input:</strong> root = [1,3,null,5,3]
# <strong>Output:</strong> 2
# <strong>Explanation:</strong> The maximum width existing in the third level
# with the length 2 (5,3).
# </pre>
# 
# <p><strong>Example 3:</strong></p>
# <img alt=""
# src="https://assets.leetcode.com/uploads/2021/05/03/width3-tree.jpg"
# style="width: 289px; height: 299px;" />
# <pre>
# <strong>Input:</strong> root = [1,3,2,5]
# <strong>Output:</strong> 2
# <strong>Explanation:</strong> The maximum width existing in the second level
# with the length 2 (3,2).
# </pre>
# 
# <p><strong>Example 4:</strong></p>
# <img alt=""
# src="https://assets.leetcode.com/uploads/2021/05/03/width4-tree.jpg"
# style="width: 500px; height: 244px;" />
# <pre>
# <strong>Input:</strong> root = [1,3,2,5,null,null,9,6,null,null,7]
# <strong>Output:</strong> 8
# <strong>Explanation:</strong> The maximum width existing in the fourth level
# with the length 8 (6,null,null,null,null,null,null,7).
# </pre>
# 
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# 
# <ul>
# <li>The number of nodes in the tree is in the range <code>[1,
# 3000]</code>.</li>
# <li><code>-100 &lt;= Node.val &lt;= 100</code></li>
# </ul>
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        self.max_width = 1
        levelmap = {}
        def traverse(root, hd, level):
            if(not root):
                return
            traverse(root.left, 2 * hd - 1, level + 1)
            traverse(root.right, 2 * hd, level + 1)
            if(level not in levelmap):
                levelmap[level] = hd
            else:
                self.max_width = max(self.max_width, abs(levelmap[level] - hd) + 1)
                levelmap[level] = min(levelmap[level], hd)
        traverse(root, 1, 0)
        return self.max_width
        
