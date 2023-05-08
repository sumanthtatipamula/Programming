# n = int(input())
# denominations = [1, 5, 10, 20, 100]
# dp = [float("Inf")] * (n + 1) 
# dp[0] = 0
# for i in range(1, len(denominations) + 1):
#     for j in range(denominations[i - 1], n + 1):
#         dp[j] = min(dp[j],  1 + dp[j - denominations[i - 1]])
# print(dp[n])

n = int(input())
denominations = [1, 5, 10, 20, 100]
count = 0
for i in range(len(denominations) - 1, -1, -1):
    if(n >= denominations[i]):
        count += (n // denominations[i])
        n %= denominations[i]
print(count)