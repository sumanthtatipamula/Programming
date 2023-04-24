#User function Template for python3
class Solution:
	def minSteps(self, n):
		 dp = [0] * (n + 1)
		 for i in range(2, n + 1):
		     dp[i] = dp[i - 1] + 1
		     if(i % 2 == 0):
		         dp[i] = min(dp[i], dp[i // 2] + 1)
	         if(i % 3 == 0):
	             dp[i] = min(dp[i], dp[i // 3] + 1)
         return dp[n]
             
		 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.minSteps(N)
		print(ans)

# } Driver Code Ends