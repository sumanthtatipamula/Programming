string  = input()
queries = int(input())
dp = [0] * len(string)
for i in range(1, len(string)):
    dp[i] = dp[i - 1]
    if(string[i] == string[i - 1]):
        dp[i] += 1
for i in range(queries):
    left, right = map(int, input().split())
    print(dp[right - 1] - dp[left - 1])