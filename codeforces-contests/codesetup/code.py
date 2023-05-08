from math import ceil, floor
import sys, os
sys.stdin = open(os.path.join(sys.path[0], "input.txt"), "r")
sys.stdout = open(os.path.join(sys.path[0], "output.txt"), "w")

from collections import defaultdict

n = int(input())
denominations = [1, 5, 10, 20, 100]
count = 0
for i in range(len(denominations) - 1, -1, -1):
    if(n >= denominations[i]):
        count += (n // denominations[i])
        n %= denominations[i]
print(count)




    


