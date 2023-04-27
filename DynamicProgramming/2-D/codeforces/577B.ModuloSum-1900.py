"""
3 5
1 2 3
"""

n, m = map(int, input().split())
arr = list(map(int, input().split()))
### for n > m case if u take prefix sum of the array and modulo for each element in that case since n > m there will be two repeating mod values which indicates elements between those indices are divisible by m 
# the pigeonhole principle states that if n items are put into m containers, with n > m, then at least one container must contain more than one item.
isDivisible = True;
if(n < m):
    dp = [[False] * (m) for i in range(2)]
    for i in range(1, n + 1):
        mod_val = (arr[i - 1] % m)
        dp[1][mod_val] = True
        for j in range(1, m):
            if(dp[0][j] == True):
                dp[1][ (j + mod_val) % m] = True
        for j in range(m):
            dp[0][j] = dp[1][j]
    isDivisible = dp[1][0];
print("YES" if(isDivisible) else "NO")

