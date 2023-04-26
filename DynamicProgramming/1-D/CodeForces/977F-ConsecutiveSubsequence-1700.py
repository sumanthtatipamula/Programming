"""
https://codeforces.com/problemset/problem/977/F
"""
from collections import defaultdict


n = int(input())
arr = list(map(int, input().split()))
map = defaultdict(int)
max_elements = 0
max_index = 0
for index, val in enumerate(arr):
    map[val] = 1 + map[val - 1]
    if(map[val] > max_elements):
        max_elements = map[val]
        max_index = index
print(max_elements)
ending_element = arr[max_index] - max_elements + 1
for i in range(0, max_index + 1):
    if(arr[i] == ending_element):
        ending_element += 1
        print(i + 1, end = ' ')





