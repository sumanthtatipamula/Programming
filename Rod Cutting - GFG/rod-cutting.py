#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        memo = {}
        def traverse(length):
            if(length == 0):
                return 0
            if(length in memo):
                return memo[length]
            profit = 0
            for i in range(1, length + 1):
                profit = max(profit, price[i - 1] + traverse(length - i))
            memo[length] = profit
            return memo[length]
        return traverse(n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends