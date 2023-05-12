n, string = int(input()), input()
max_length, count = 0,0 
map = {0 : -1}
for i in range(0, len(string)):
    count += 1 if(string[i] == '1') else -1
    if(count in map):
        max_length = max(max_length, i - map[count])
    else:
        map[count] = i
print(max_length)