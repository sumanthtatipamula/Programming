n, k = map(int, input().split())
elements = list(map(int, input().split()))
min_index, total, current_sum = -1, float("Inf"), 0
k -= 1
for i in range(n):
    current_sum += elements[i]
    if(i >= k):
        if(current_sum < total):
            total = current_sum
            min_index = i - k
        current_sum -= elements[i - k]
print(min_index + 1)