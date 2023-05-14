n, l = map(int, input().split())
laterns = list(map(int, input().split()))
laterns.sort()
max_distance = 0
for i in range(1, n):
    max_distance = max(max_distance, laterns[i] - laterns[i - 1])
print(max(max_distance / 2, laterns[0] -  0, l - laterns[n - 1]))