#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        map = {0 : -1}
        max_length = 0
        sum = 0
        for index, value in enumerate(arr):
            sum += value;
            if(sum in map):
                max_length = max(max_length, index - map[sum])
            else:
                map[sum] = index
        return max_length;
        


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends