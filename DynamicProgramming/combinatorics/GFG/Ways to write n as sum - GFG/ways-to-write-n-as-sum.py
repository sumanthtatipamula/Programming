#User function Template for python3

class Solution:
    #Function to count the number of different ways in which n can be 
    #written as a sum of two or more positive integers.
    def countWays(self,n):
        if(n <= 3):
            return n - 1
        mod = 1000000007
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n):
            for j in range(i, n + 1):
                dp[j] = (dp[j - i] + dp[j]) % mod
        # print(dp)
        return dp[n]
                
        
        
        # code here


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
        ob=Solution()
        print(ob.countWays(n))

# } Driver Code Ends