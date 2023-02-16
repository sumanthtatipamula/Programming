
class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
		def canFindDestination(i, j):
            if(i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0):
                return False;
            if(grid[i][j] == 2):
                return True
            grid[i][j] = 0
            found = False
            for k in range(-1, 2, 2):
                found  = found or canFindDestination(i + k, j)  or canFindDestination(i, j + k) 
                if(found):
                    return True
            return found
		for i in range(0, len(grid)):
		    for j in range(0, len(grid[0])):
		        if(grid[i][j] == 1):
		            if(canFindDestination(i, j)):
		                return True
	                return False
        
            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.is_Possible(grid)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends