for _ in range(int(input())):
    n  = int(input())
    elements = list(map(int, input().split()))
    rem = [0, 0, 0]
    for element in elements:
        rem[element % 3] += 1
    print(rem[0] + min(rem[1], rem[2]) +  (max(rem[1], rem[2]) - min(rem[1], rem[2])) // 3)
    