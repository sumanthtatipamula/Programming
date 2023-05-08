# n, l, r = map(int, input().split())
# mod = 10 ** 9 + 7
# mem = {}
# def find_ways(index, sum_so_far):
#     if(index == n):
#         return sum_so_far % 3  == 0
#     ways = 0
#     if((index, sum_so_far) in mem):
#         return mem[(index, sum_so_far)]
#     for i in range(l, r + 1):
#         ways = (ways + find_ways(index + 1, sum_so_far + i)) % mod
#     mem[(index, sum_so_far)] = ways
#     return ways

# print(find_ways(0, 0))

n, l, r = map(int, input().split())
mod = 10 ** 9 + 7
dp = [[0] * (3) for _ in range(n + 1)]
numbers = [
    r // 3 - (l - 1) // 3,
    (r + 2) // 3 - (l + 1) // 3,
    (r + 1) // 3 - l // 3
]
dp[0][0] = 1
for i in range(n):
    dp[i + 1][0] = ((dp[i][0] * numbers[0]) % mod + (dp[i][1] * numbers[2]) % mod + (dp[i][2] * numbers[1]) % mod) % mod
    dp[i + 1][1] = (dp[i][1] * numbers[0] + dp[i][0] * numbers[1] + dp[i][2] * numbers[2]) % mod
    dp[i + 1][2] = (dp[i][2] * numbers[0] + dp[i][1] * numbers[1] + dp[i][0] * numbers[2]) % mod

print(dp[n][0])