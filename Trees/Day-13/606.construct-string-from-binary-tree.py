#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#
# https://leetcode.com/problems/construct-string-from-binary-tree/description/
#
# algorithms
# Easy (56.58%)
# Total Accepted:    115.1K
# Total Submissions: 202.9K
# Testcase Example:  '[1,2,3,4]'
#
# <p>Given the <code>root</code> of a binary tree, construct a string consists
# of parenthesis and integers from a binary tree with the preorder traversing
# way, and return it.</p>
# 
# <p>Omit all the empty parenthesis pairs that do not affect the one-to-one
# mapping relationship between the string and the original binary tree.</p>
# 
# <p>&nbsp;</p>
# <p><strong>Example 1:</strong></p>
# <img alt=""
# src="https://assets.leetcode.com/uploads/2021/05/03/cons1-tree.jpg"
# style="width: 292px; height: 301px;" />
# <pre>
# <strong>Input:</strong> root = [1,2,3,4]
# <strong>Output:</strong> &quot;1(2(4))(3)&quot;
# <strong>Explanation:</strong> Originallay it needs to be
# &quot;1(2(4)())(3()())&quot;, but you need to omit all the unnecessary empty
# parenthesis pairs. And it will be &quot;1(2(4))(3)&quot;
# </pre>
# 
# <p><strong>Example 2:</strong></p>
# <img alt=""
# src="https://assets.leetcode.com/uploads/2021/05/03/cons2-tree.jpg"
# style="width: 207px; height: 293px;" />
# <pre>
# <strong>Input:</strong> root = [1,2,3,null,4]
# <strong>Output:</strong> &quot;1(2()(4))(3)&quot;
# Explanation: Almost the same as the first example, except we cannot omit the
# first parenthesis pair to break the one-to-one mapping relationship between
# the input and the output.
# </pre>
# 
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# 
# <ul>
# <li>The number of nodes in the tree is in the range <code>[1,
# 10<sup>4</sup>]</code>.</li>
# <li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def traverse(root):
            if(not root):
                return ''
            if(not root.left and not root.right):
                return str(root.val)
            return str(root.val) + '(' + traverse(root.left) + ')' + ('' if(not root.right) else '(' + traverse(root.right) + ')')
        return traverse(root)
        
