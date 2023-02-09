#
# @lc app=leetcode id=1261 lang=python
#
# [1261] Find Elements in a Contaminated Binary Tree
#
# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/
#
# algorithms
# Medium (76.16%)
# Likes:    826
# Dislikes: 90
# Total Accepted:    53.5K
# Total Submissions: 70.1K
# Testcase Example:  '["FindElements","find","find"]\n[[[-1,null,-1]],[1],[2]]'
#
# Given a binary tree with the following rules:
# 
# 
# root.val == 0
# If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 *
# x + 1
# If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2
# * x + 2
# 
# 
# Now the binary tree is contaminated, which means all treeNode.val have been
# changed to -1.
# 
# Implement the FindElements class:
# 
# 
# FindElements(TreeNode* root) Initializes the object with a contaminated
# binary tree and recovers it.
# bool find(int target) Returns true if the target value exists in the
# recovered binary tree.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["FindElements","find","find"]
# [[[-1,null,-1]],[1],[2]]
# Output
# [null,false,true]
# Explanation
# FindElements findElements = new FindElements([-1,null,-1]); 
# findElements.find(1); // return False 
# findElements.find(2); // return True 
# 
# Example 2:
# 
# 
# Input
# ["FindElements","find","find","find"]
# [[[-1,-1,-1,-1,-1]],[1],[3],[5]]
# Output
# [null,true,true,false]
# Explanation
# FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
# findElements.find(1); // return True
# findElements.find(3); // return True
# findElements.find(5); // return False
# 
# Example 3:
# 
# 
# Input
# ["FindElements","find","find","find","find"]
# [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
# Output
# [null,true,false,false,true]
# Explanation
# FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
# findElements.find(2); // return True
# findElements.find(3); // return False
# findElements.find(4); // return False
# findElements.find(5); // return True
# 
# 
# 
# Constraints:
# 
# 
# TreeNode.val == -1
# The height of the binary tree is less than or equal to 20
# The total number of nodes is between [1, 10^4]
# Total calls of find() is between [1, 10^4]
# 0 <= target <= 10^6
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
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.construct(root, 0)

    def construct(self, root, value):
        if(not root):
            return None
        root.val = value
        self.construct(root.left, 2 * value + 1)
        self.construct(root.right, 2 * value + 2)
        

    def find(self, target: int) -> bool:
        index, binary, root = 0, bin(target + 1)[3:], self.root
        while(root and index <= len(binary)):
            if(root.val == target):
                return True
            if(binary[index] == '0'):
                root = root.left
            else:
                root = root.right
            index += 1
        return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end

