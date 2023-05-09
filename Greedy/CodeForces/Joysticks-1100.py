a1, a2 = map(int, input().split())
count = 0
while(a1 > 0 and a2 > 0):
    if(a1 < a2):
        a1 += 1
        a2 -= 2
    else:
        a1 -= 2
        a2 += 1
    if(a1 >= 0 and a2 >= 0):
        count += 1
print(count)
