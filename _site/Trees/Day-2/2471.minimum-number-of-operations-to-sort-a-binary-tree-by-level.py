#
# @lc app=leetcode id=2471 lang=python
#
# [2471] Minimum Number of Operations to Sort a Binary Tree by Level
#
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/
#
# algorithms
# Medium (62.42%)
# Likes:    365
# Dislikes: 9
# Total Accepted:    14.5K
# Total Submissions: 23.2K
# Testcase Example:  '[1,4,3,7,6,8,5,null,null,null,null,9,null,10]'
#
# You are given the root of a binary tree with unique values.
# 
# In one operation, you can choose any two nodes at the same level and swap
# their values.
# 
# Return the minimum number of operations needed to make the values at each
# level sorted in a strictly increasing order.
# 
# The level of a node is the number of edges along the path between it and the
# root node.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
# Output: 3
# Explanation:
# - Swap 4 and 3. The 2^nd level becomes [3,4].
# - Swap 7 and 5. The 3^rd level becomes [5,6,8,7].
# - Swap 8 and 7. The 3^rd level becomes [5,6,7,8].
# We used 3 operations so return 3.
# It can be proven that 3 is the minimum number of operations needed.
# 
# 
# Example 2:
# 
# 
# Input: root = [1,3,2,7,6,5,4]
# Output: 3
# Explanation:
# - Swap 3 and 2. The 2^nd level becomes [2,3].
# - Swap 7 and 4. The 3^rd level becomes [4,6,5,7].
# - Swap 6 and 5. The 3^rd level becomes [4,5,6,7].
# We used 3 operations so return 3.
# It can be proven that 3 is the minimum number of operations needed.
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2,3,4,5,6]
# Output: 0
# Explanation: Each level is already sorted in increasing order so return
# 0.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^5].
# 1 <= Node.val <= 10^5
# All the values of the tree are unique.
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
import collections
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        nodes, count = deque([root]), 0
        
        def perm(arr):                                            
            pos = {m:j for j,m in enumerate(sorted(arr))}         
            vis, tot = [0] * len(arr), 0                         
            for i in range(len(arr)):                             
                cnt = 0
                while not vis[i] and i != pos[arr[i]]:            
                    vis[i], i = 1, pos[arr[i]]                   
                    cnt += 1                                      
                tot += max(0, cnt-1)                              
            return tot
                    
        while nodes:
            vals = []
            for _ in range(len(nodes)):                           
                n = nodes.popleft()                               
                vals.append(n.val)                                 
                if n.left  : nodes.append(n.left)
                if n.right : nodes.append(n.right)
            count += perm(vals)                                   
            
        return count
        
# @lc code=end

