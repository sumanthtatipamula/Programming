from collections import defaultdict


n = int(input())
elements = list(map(int , input().split()))
max_count, max_index = 0, -1
map = defaultdict(int)
for i in range(0, n):
    map[elements[i]] = map[elements[i] - 1] + 1
    if(map[elements[i]] > max_count):
        max_count = map[elements[i]]
        max_index = i
print(max_count)
start = elements[max_index] - max_count + 1 
for i in range(0, max_index + 1):
    if(elements[i] == start):
        print(i + 1 , end= " ")
        start += 1
