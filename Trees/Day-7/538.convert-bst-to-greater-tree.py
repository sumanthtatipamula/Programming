# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        global gSum
        def convert(root, sum_so_far):
            global gSum
            if(not root):
                return 0
            convert(root.right, sum_so_far)
            root.val += gSum
            gSum = root.val
            convert(root.left, root.val)
        gSum = 0
        convert(root, 0)
        return root