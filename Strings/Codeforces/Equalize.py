length = int(input())
s, t = input(), input()
count = 0
right = 0
while(right < length):
    if(s[right] != t[right]):
        if(right < length - 1 and s[right] != s[right + 1]):
            count += 1
            right += 1
        else:
            count += 1
    right += 1
print(count)