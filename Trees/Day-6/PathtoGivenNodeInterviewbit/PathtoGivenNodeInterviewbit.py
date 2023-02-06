# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, root, element):
        result = []
        def traverse(root):
            if(not root):
                return False
            if(root.val == element):
                result.append(root.val)
                return True
            found_left = traverse(root.left)
            found_right = traverse(root.right)
            if(found_left or found_right):
                result.append(root.val)
                return True
            return False
        traverse(root)
        return result[::-1]
        