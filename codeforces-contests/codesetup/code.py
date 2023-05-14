import sys, os
sys.stdin = open(os.path.join(sys.path[0], "input.txt"), "r")
sys.stdout = open(os.path.join(sys.path[0], "output.txt"), "w")

# import sys
# input = sys.stdin.readline
from math import ceil
from functools import lru_cache

n, m, a, b = map(int, input().split())
mem = {}
@lru_cache(maxsize= None)
def find_min_cost(days, current_day):
    if(current_day >= days):
        return 0
    if(current_day in mem):
        return mem[current_day]
    mem[current_day]  = min(a + find_min_cost(days, current_day + 1), b + find_min_cost(days, current_day + m))
    return mem[current_day]
print(find_min_cost(n, 0))

