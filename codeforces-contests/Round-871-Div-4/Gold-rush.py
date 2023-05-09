global mem;
def isPossible(n, m):
    if(n == m):
        return True
    if(n < m or n % 3 != 0):
        return False
    if(n in mem):
        return mem[n]
    mem[n] = isPossible(n // 3, m) or isPossible(2 * (n // 3), m)
    return mem[n]

for _ in range(int(input())):
    mem = {}
    n, m = map(int, input().split())
    if(isPossible(n, m)):
        print("YES")
    else:
        print("NO")