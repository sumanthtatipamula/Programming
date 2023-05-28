class Solution:
    def minimumCost(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if(s[i] != s[i - 1]):
                dp[i] = dp[i - 1] + i
            else:
                dp[i] = dp[i - 1]
        result = dp[-1]
        right = 0
        for j in range(len(s) - 2, -1, -1):
            if(s[j] != s[j + 1]):
                right += (len(s) - j - 1)
            result = min(result, right + dp[j])
        return result

