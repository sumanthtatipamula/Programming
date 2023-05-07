for _ in range(int(input())):
    length = int(input())
    elements = list(map(int, input().split()))
    count, max_count = 0, 0
    for binary in elements:
        if(binary == 0):
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)
    print(max_count)