n, k = map(int, input().split())
string = input()
letters = set(map(str, input().split()))
count_sub_strings, prev = 0, 0
for i in range(n):
    if(string[i] not in letters):
        substring_length = i - prev
        count_sub_strings += ((substring_length) * (substring_length + 1)) // 2
        prev = i + 1

substring_length = n - prev
count_sub_strings += ((substring_length) * (substring_length + 1)) // 2
print(count_sub_strings)