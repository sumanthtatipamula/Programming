import sys, os
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())
elements = list(map(int, input().split()))
dp = [0] * (n)
dp[0] = 1 if(elements[0] < 0) else 0
for i in range(1, n):
    dp[i] = dp[i - 1]
    if(elements[i] < 0):
        dp[i] += 1

changes = float("Inf")
right_pos = 1 if(elements[n - 1] > 0) else 0
for i in range(n - 2, -1, -1):
    current_as_peak = i - dp[i] + (n - i - right_pos)
    changes = min(changes, current_as_peak)
    if(elements[i] > 0):
        right_pos += 1
print(changes)