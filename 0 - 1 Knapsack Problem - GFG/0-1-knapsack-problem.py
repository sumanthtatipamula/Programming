#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, size, weight, value, n):
        dp = [0] * (size + 1)
        for i in range(1, n + 1):
            for j in range(size, weight[i - 1] - 1, -1):
                    dp[j] = max(dp[j], dp[j - weight[i - 1]] + value[i - 1])
        return dp[size]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends