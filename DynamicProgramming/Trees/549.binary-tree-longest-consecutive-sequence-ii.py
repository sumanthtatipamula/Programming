# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_length = [1]
        def dfs(root):
            if(not root):
                return [0, 0]
            if(not root.left and not root.right):
                return [1, 1]
            left = dfs(root.left)
            left[0], left[1] = left[0] + 1, left[1] + 1
            right = dfs(root.right)
            right[0], right[1] = right[0] + 1, right[1] + 1
            if(root.left):
                if(root.left.val + 1 != root.val):
                    left[0] = 1
                if(root.left.val - 1 != root.val):
                    left[-1] = 1
            if(root.right):
                if(root.right.val + 1 != root.val):
                    right[0] = 1
                if(root.right.val - 1 != root.val):
                    right[-1] = 1
            max_length[0] = max(left[0] + right[-1] - 1, max_length[0], left[1] + right[0] - 1)
            return [max(left[0], right[0]), max(left[1], right[1])]
        dfs(root)
        return max_length[0]