# import sys
# input = sys.stdin.readline
    

# for _ in range(int(input())):
#     n, k = list(map(int, input().split()))
#     elements = list(map(int, input().split()))
#     elements.sort()
#     mem = {}
#     left, right = 0, len(elements) - 1
#     def find_max_sum(left, right, k):
#         if(left > right):
#             return 0
#         if(k == 0):
#             return sum(elements[left: right + 1])
#         if((left, right) in mem):
#             return mem[(left, right)]
#         k -= 1
#         mem[(left, right)] = max(find_max_sum(left + 2, right, k), find_max_sum(left, right - 1, k))
#         return mem[(left, right)]       
#     print(find_max_sum(0, len(elements) - 1, k))

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    elements = list(map(int, input().split()))
    elements.sort()
    prefix = [0] * (n + 1)
    for i in range(1, len(elements) + 1):
        prefix[i] = prefix[i - 1] + elements[i - 1]
    result = 0
    for x in range(0, k + 1):
        result = max(prefix[n - (k - x)] - prefix[2 * x], result)
    print(result)