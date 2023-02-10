#
# @lc app=leetcode id=919 lang=python
#
# [919] Complete Binary Tree Inserter
#
# https://leetcode.com/problems/complete-binary-tree-inserter/description/
#
# algorithms
# Medium (65.05%)
# Likes:    938
# Dislikes: 86
# Total Accepted:    44.4K
# Total Submissions: 68.3K
# Testcase Example:  '["CBTInserter","insert","insert","get_root"]\n[[[1,2]],[3],[4],[]]'
#
# A complete binary tree is a binary tree in which every level, except possibly
# the last, is completely filled, and all nodes are as far left as possible.
# 
# Design an algorithm to insert a new node to a complete binary tree keeping it
# complete after the insertion.
# 
# Implement the CBTInserter class:
# 
# 
# CBTInserter(TreeNode root) Initializes the data structure with the root of
# the complete binary tree.
# int insert(int v) Inserts a TreeNode into the tree with value Node.val == val
# so that the tree remains complete, and returns the value of the parent of the
# inserted TreeNode.
# TreeNode get_root() Returns the root node of the tree.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["CBTInserter", "insert", "insert", "get_root"]
# [[[1, 2]], [3], [4], []]
# Output
# [null, 1, 2, [1, 2, 3, 4]]
# 
# Explanation
# CBTInserter cBTInserter = new CBTInserter([1, 2]);
# cBTInserter.insert(3);  // return 1
# cBTInserter.insert(4);  // return 2
# cBTInserter.get_root(); // return [1, 2, 3, 4]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree will be in the range [1, 1000].
# 0 <= Node.val <= 5000
# root is a complete binary tree.
# 0 <= val <= 5000
# At most 10^4 calls will be made to insert and get_root.
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
class CBTInserter:
    root = None
    insertionQueue = deque()
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.insertionQueue = deque()
        queue = deque([root])
        while(queue):
            node = queue.popleft()
            if(not node.left or not node.right):
                self.insertionQueue.append(node)
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)



    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        parent = self.insertionQueue[0].val
        if(not self.insertionQueue[0].left):
            self.insertionQueue[0].left = new_node
        elif(not self.insertionQueue[0].right):
            self.insertionQueue[0].right = new_node
            self.insertionQueue.popleft()
        self.insertionQueue.append(new_node)
        return parent
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
# @lc code=end

