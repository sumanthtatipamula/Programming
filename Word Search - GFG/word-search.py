class Solution:
	def isWordExist(self, board, word):
		def dfs(x, y, i):
		    if(i == len(word)):
		        #print(x,y,i, len(word))
		        return True
	        if(x < 0 or y < 0 or x == len(board) or y == len(board[0]) or board[x][y] != word[i]):
	            return False
            board[x][y] = '_'
	        for k in range(-1, 2, 2):
	            if(dfs(x + k, y, i + 1) or dfs(x, y + k, i + 1)):
	                return True
            board[x][y] = word[i]
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == word[0] and dfs(i,j,0)):
                    return True
        return False
	            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n, m = map(int, input().split())
		board = []
		for i in range(n):
			a = list(input().strip().split())
			b = []
			for j in range(m):
				b.append(a[j][0])
			board.append(b)
		word = input().strip()
		obj = Solution()
		ans = obj.isWordExist(board, word)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends