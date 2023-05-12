for _ in range(int(input())):
    n, x  = map(int, input().split())
    nums = list(map(int, input().split()))
    max_dp = [0] * (n + 1)
    dp = [0] * (n + 1) 
    for i in range(1, n + 1):
        for j in range(n, -1, -1):
            if(j == 0):
                dp[j] = max(nums[i - 1], nums[i - 1] + dp[j])
            else:
                dp[j] = max(nums[i - 1] + x, nums[i - 1] + x + dp[j - 1], nums[i - 1] + dp[j])
            max_dp[j] = max(max_dp[j], dp[j])
    print(*max_dp)