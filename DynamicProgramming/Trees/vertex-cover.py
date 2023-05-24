from collections import defaultdict

n = int(input())
adj = defaultdict(list)
dp = [[0] * 2 for _ in range(n + 1)]
def find_min_vertex(source, parent):
    dp[source][0] = 0
    dp[source][1] = 1
    for child in adj[source]:
        if(child != parent):
            find_min_vertex(child, source)
            dp[source][0] += dp[child][1]
            dp[source][1] += min(dp[child][0], dp[child][1])
    

for i in range(n -  1):
    u, v =  map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

find_min_vertex(1, -1)
print(min(dp[1][1], dp[1][0]))