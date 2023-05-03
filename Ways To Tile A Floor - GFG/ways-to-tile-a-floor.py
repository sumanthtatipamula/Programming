#User function Template for python3

class Solution:
    def numberOfWays(self, n):
        a, b = 1, 2
        mod =  10 ** 9 + 7
        if(n <= 2):
            return n
        for i in range(3, n + 1):
            a, b = b, (a + b) % mod
        return b


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.numberOfWays(N))
# } Driver Code Ends