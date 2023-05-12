string = input()
first_index = string.find("AB")
ab_index_min, ab_index_max, ba_index_min, ba_index_max = len(string), -1, len(string), -1 
for i in range(0, len(string) - 1):
    if(string[i] + string[i + 1] == "AB"):
        ab_index_min = min(ab_index_min ,i)
        ab_index_max = max(ab_index_max, i)
    if(string[i] + string[i + 1] == "BA"):
        ba_index_min = min(ba_index_min ,i)
        ba_index_max = max(ba_index_max, i)
ab_index_max -= 1
ba_index_max -= 1
if(ab_index_max > ba_index_min or ba_index_max > ab_index_min):
    print("YES")
else:
    print("NO")