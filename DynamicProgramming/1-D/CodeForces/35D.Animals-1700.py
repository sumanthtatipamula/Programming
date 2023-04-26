"""
3 4
1 1 1
https://codeforces.com/contest/35/
"""

import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')
f = lambda: map(int, input().split())
n, x = f()
res = 0

for val in sorted(food * (n - i) for i, food in enumerate(f())):
    if(x < val):
        break;
    x -= val
    res += 1

print(res)
    


        

