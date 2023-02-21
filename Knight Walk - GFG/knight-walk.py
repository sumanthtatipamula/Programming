from collections import deque
class Solution:
	def minStepToReachTarget(self, knightPos, targetPos, N):
	    if(knightPos == targetPos):
	        return 0
	    r, c, queue, directions = N, N, deque([knightPos]), [(-1, 2), (1, 2), (-1, -2), (1, -2), (-2, 1), (2, 1), (-2, -1), (2, -1)]
	    level = 0
	    vis = [[0 for i in range(c + 1)] for j in range(r + 1)]
	    vis[knightPos[0]][knightPos[-1]] = 1
	    while(queue):
	        for _ in range(len(queue)):
	            x, y = queue.popleft()
	            for i, j in directions:
	                new_x, new_y = x + i, y + j
	                if(new_x == targetPos[0] and new_y == targetPos[1]):
	                    return level + 1
                    if(new_x < 0 or new_y < 0 or new_x > r or new_y > c or vis[new_x][new_y] == 1):
                        continue
                    vis[new_x][new_y] = 1
                    queue.append([new_x, new_y])
            level += 1
        return -1
	    
	


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		KnightPos = list(map(int, input().split()))
		TargetPos = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
		print(ans)

# } Driver Code Ends