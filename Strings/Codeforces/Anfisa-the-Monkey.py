k, a, b = map(int, input().split())
string = input()
splits = []
mem = {}
def find_splits(index, k):
    if(index == len(string) and k == 0):
        return True
    if(k == 0 or index == len(string)):
        return False
    if((index, k) in mem and not mem[(index, k)]):
        return False
    for i in range(a, min(b + 1, len(string) - index + 1)):
        splits.append(string[index: index + i])
        if(find_splits(index + i, k - 1)):
            return True
        splits.pop()
    mem[(index, k)] = False
    return False


if(len(string) <= k * b and len(string) >= k):
    index = 0
    find_splits(0, k)
    if(len(splits) == 0):
        print("No solution")
    for split in splits:
        print(split)
else:
    print("No solution")