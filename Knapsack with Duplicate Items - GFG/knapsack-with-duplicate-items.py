#User function Template for python3

class Solution:
    def knapSack(self, n, size, value, weight):
        dp = [0] * (size + 1)
        for i in range(1, n + 1):
            for j in range(weight[i - 1], size + 1):
                    dp[j] = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])
        return dp[size]
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends