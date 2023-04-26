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
arr = list(f())
mem = {}

def findAnimals(index, foodLeft):
    if(foodLeft == 0):
        return 0
    if(foodLeft < 0):
        return -1
    if(index == len(arr)):
        return 0 if(foodLeft > 0) else -1
    if((index, foodLeft) in mem):
        return mem[(index, foodLeft)]  
    inclusive = 1 + findAnimals(index + 1, foodLeft - (arr[index] * (n - index)))
    exclusive = findAnimals(index + 1, foodLeft)
    mem[(index, foodLeft)] = max(inclusive, exclusive)
    return mem[(index, foodLeft)] 

print(findAnimals(0, x))
    


        

