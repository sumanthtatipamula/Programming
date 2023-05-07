for _ in range(int(input())):
    length = int(input())
    dp = [float("Inf")] * 3
    for i in range(length):
        time, skill = list(map(str, input().split()))
        time = int(time)
        if(skill == "01"):
            dp[0] = min(dp[0], time)
        elif(skill == "10"):
            dp[1] = min(dp[1], time)
        elif(skill == "11"):
            dp[2] = min(dp[2], time)
    min_time = float("Inf")
    if(dp[0] != float("Inf") and dp[1] != float("Inf")):
        min_time = dp[0] + dp[1]
    if(dp[2] != float("Inf")):
        min_time = min(min_time, dp[2])
    print(-1 if(min_time == float("Inf")) else min_time)