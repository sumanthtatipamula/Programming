#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        temp = []
        for i in range(n):
            temp.append((arr[i], 1))
            temp.append((dep[i] + 1, -1))
        temp.sort()
        max_platforms, curr = 0,0
        for i in range(len(temp)):
            curr += temp[i][1]
            max_platforms = max(max_platforms, curr)
        return max_platforms
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends