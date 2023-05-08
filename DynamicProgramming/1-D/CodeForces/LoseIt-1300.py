from collections import defaultdict

n = (int(input()))
elements = list(map(int, input().split()))
act = [4,8,15,16,23,42]
freq, result = defaultdict(int), 0
for element in elements:
    curr_freq = freq[element] + 1
    extra_element = False
    for j in range(act.index(element) - 1, -1 , -1):
        if(curr_freq > freq[act[j]]):
            extra_element = True
    if(extra_element):
        result += 1
    else:
        freq[element] += 1
min_subsequences = float("Inf")
for element in act:
    min_subsequences = min(min_subsequences, freq[element])
for element in act:
    result += freq[element] - min_subsequences
print(result)