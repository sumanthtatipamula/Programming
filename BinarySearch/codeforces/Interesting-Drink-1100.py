from bisect import bisect_right
n = int(input())
elements = list(map(int, input().split()))
elements.sort()
for i in range(int(input())):
    print(bisect_right(elements, int(input())))