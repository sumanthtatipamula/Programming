for _ in range(int(input())):
    n, count, prev = int(input()), 0, -1
    while(prev != n):
        prev = n
        if(n % 5 == 0):
            n = 4 * (n // 5)
        elif(n % 3 == 0):
            n = 2 * (n // 3)
        elif(n % 2 == 0):
            n = n // 2
        count += 1
    print(count - 1 if(n == 1) else -1)