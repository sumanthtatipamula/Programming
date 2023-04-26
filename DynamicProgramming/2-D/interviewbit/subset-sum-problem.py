class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, arr, total):
        mem = {}
        def traverse(index, total):
            if(total == 0):
                return True
            if(total < 0 or index == len(arr)):
                return False
            if((index, total) in mem):
                return mem[(index, total)]
            inclusive = traverse(index + 1, total - arr[index])
            exclusive = traverse(index + 1, total)
            mem[(index, total)] = inclusive or exclusive
            return mem[(index, total)]
        return 1 if(traverse(0, total)) else 0

    def solve(self, arr, total):
        dp = [[0 for i in range(total + 1)] for j in range(len(arr) + 1)]
        dp[0][0] = 1
        for i in range(1, len(arr) + 1):
            for j in range(0, total + 1):
                dp[i][j] = dp[i - 1][j]
                if(j >= arr[i - 1]):
                    dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]
        return dp[len(arr)][total]