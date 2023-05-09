n,  money = map(int, input().split())
elements = list(map(int , input().split()))
count_even = 0
mem = {}
def makeSplits(index, even_count, money):
    if(index == n - 1):
        return 0
    if(elements[index] % 2 == 0):
        even_count += 1
    if((index, money) in mem):
        return mem[(index, money)]
    max_cuts = makeSplits(index + 1, even_count, money)
    if(even_count == (index + 1) - even_count and money >= abs(elements[index] - elements[index + 1])):
        max_cuts = max(max_cuts, 1 + makeSplits(index + 1, even_count, money - abs(elements[index] - elements[index + 1])))
    mem[(index, money)] = max_cuts
    return max_cuts

print(makeSplits(0, 0, money))