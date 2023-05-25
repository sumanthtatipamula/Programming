class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 0 - inclusive 1 - exclusive
        def dfs(root):
            if(not root):
                return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            inc, exc = root.val + left[-1] + right[-1], max(left) + max(right)
            return [inc, exc]
        return max(dfs(root))