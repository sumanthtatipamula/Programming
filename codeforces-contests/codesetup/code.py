# import sys, os
# sys.stdin = open(os.path.join(sys.path[0], "input.txt"), "r")
# sys.stdout = open(os.path.join(sys.path[0], "output.txt"), "w")

# import sys
# input = sys.stdin.readline

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








        







    


