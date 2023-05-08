from math import ceil, floor
import sys, os
sys.stdin = open(os.path.join(sys.path[0], "input.txt"), "r")
sys.stdout = open(os.path.join(sys.path[0], "output.txt"), "w")

for _ in range(int(input())):
    n = int(input())
    elements = list(map(int, input().split()))
    mem = {}
    def findProfit(index):
        if(index > len(elements)):
            return 0
        if(index in mem):
            return mem[index]
        profit = elements[index - 1] + findProfit(index + elements[index - 1])
        mem[index] = profit
        return profit
    max_profit = 0
    for i in range(n, 0, -1):
        max_profit = max(max_profit, findProfit(i))
    print(max_profit)

    



