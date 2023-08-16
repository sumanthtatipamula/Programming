

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
	    new_nums = []
		for index, num in enumerate(nums):
		    new_nums.append((num, index))
	    new_nums.sort(key = lambda x: x[0])
	    vis = [False] * (len(nums))
	    result = 0
	    for i in range(len(nums)):
	        if(i == new_nums[i][-1] or vis[i]):
	            continue;
            elements_to_swap = 1
            curr = new_nums[i][-1]
            vis[i] = True
            while(i != curr):
                elements_to_swap += 1
                vis[curr] = True
                curr = new_nums[curr][-1]
            result += elements_to_swap - 1
        return result

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends