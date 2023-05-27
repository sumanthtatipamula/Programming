# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = -float("Inf")
        def dfs(root):
            if(not root):
                return -float("Inf")
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            self.result = max(left + right + root.val, self.result)
            return max(left + root.val, right + root.val)
        dfs(root)
        return self.result
        
