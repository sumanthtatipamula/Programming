def isPossible(n, m):
    if(n == m):
        return True
    elif(n % 3 != 0):
        return False
    return isPossible(n // 3, m) or isPossible(2 * (n // 3), m)

for _ in range(int(input())):
    n, m =  map(int, input().split())
    if(isPossible(n, m)):
        print("YES")
    else:
        print("NO")