n = int(input())
elements = list(map(int, input().split()))
dp = [[0, 0] for _ in range(n + 1)]
result = [0, 0]
for i in range(1, n + 1):
    if(elements[i - 1] == 0):
        continue;
    if(elements[i - 1] > 0):
        dp[i][0] = dp[i - 1][0] + 1
        dp[i][1] = dp[i - 1][1]
    else:
        dp[i][0] = dp[i - 1][1]
        dp[i][1] = dp[i - 1][0] + 1
    result[0] += dp[i][0]
    result[1] += dp[i][1]

print(str(result[1]) + " " + str(result[0]))