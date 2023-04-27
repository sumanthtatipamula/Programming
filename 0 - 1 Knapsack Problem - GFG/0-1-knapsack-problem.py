#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, size, weight, value, n):
        mem = {}
        def fillBag(index, remSize):
            if(index == n):
                return 0
            inclusive = 0
            if((index, remSize) in mem):
                return mem[(index, remSize)]
            if(remSize >= weight[index]):
                inclusive = value[index] + fillBag(index + 1, remSize - weight[index])
            exclusive = fillBag(index + 1 , remSize)
            mem[(index,remSize)] = max(inclusive, exclusive)
            return mem[(index, remSize)]
        return fillBag(0, size)
            


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