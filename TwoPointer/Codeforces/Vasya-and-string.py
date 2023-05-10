n,  k = map(int, input().split()) 
string = input()
if(n == 1):
    print(1)
else:
    left, right, max_length  = -1, 0, 0
    dp = [0, 0]
    while(right < len(string)):
        dp[ord(string[right]) - ord('a')] += 1
        while(min(dp) > k):
            left += 1
            dp[ord(string[left]) - ord('a')] -=1
        max_length = max(max_length, right - left)
        right += 1
    print(max(max_length, right - left - 1))
