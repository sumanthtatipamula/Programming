#User function Template for python3

class Solution:
    def countFriendsPairings(self, n):
        mem, mod = {}, 10 ** 9 + 7
        def ways(n):
            if(n <= 1):
                return 1
            if(n in mem):
                return mem[n]
            mem[n] = (ways(n - 1) + (n - 1) * ways(n - 2)) % mod
            return mem[n]
        return ways(n)
        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.countFriendsPairings(n))
# } Driver Code Ends