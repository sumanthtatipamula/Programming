class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = [[float("Inf")] * (len(arr) + 1) for _ in range(len(arr) + 1)]
        for i in range(len(arr)):
            dp[i][i] = 0
        for i in range(len(arr) - 1, -1, -1):
            for j in range(i + 1, len(arr)):
                if(j == i + 1):
                    dp[i][j] = arr[i] * arr[j]
                    continue
                for k in range(i, j, 1):
                    dp[i][j] = min(dp[i][j], max(arr[i: k + 1]) * max(arr[k + 1: j + 1]) + dp[i][k] + dp[k + 1][j])
            # print(dp[i])
        return dp[0][len(arr) - 1]
