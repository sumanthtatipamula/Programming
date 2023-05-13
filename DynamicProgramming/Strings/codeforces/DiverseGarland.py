import sys
input = sys.stdin.readline
 
n = int(input())
string = input()
index, result, count = 1, "", 0
dp =  [([0] * 3) for _ in range(n + 1)]
color_map = {'R': 0, 'G': 1, 'B': 2, 0 : 'R', 1: 'G', 2: 'B'}
for i in range(1, n + 1):
    current_color = color_map[string[i - 1]]
    for j in range(0, 3):
        dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + (0 if(current_color == j) else 1)
min_index = 0
for i in range(0, 3):
    if(dp[n][min_index] > dp[n][i]):
        min_index = i
 
print(dp[n][min_index])
result += color_map[min_index]
 
for i in range(n - 1, 0, -1):
    if(dp[i][(min_index + 1) % 3] < dp[i][(min_index + 2) % 3]):
        min_index = (min_index + 1) % 3
    else:
        min_index = (min_index + 2) % 3
    result = color_map[min_index] + result
print(result)