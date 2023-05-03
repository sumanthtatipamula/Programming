#User function Template for python3

class Solution:
    def countWays(self, n):
        mod = 10 ** 9 + 7
        if(n <= 2):
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        for i in range(4, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 3] + dp[i - 4]) % mod
        return dp[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countWays(N))
# } Driver Code Ends