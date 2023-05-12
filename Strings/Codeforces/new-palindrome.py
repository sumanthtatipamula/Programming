import sys
input = sys.stdin.readline
        
from collections import defaultdict
for _ in range(int(input())):
    string, prevLetter = input(), None
    map, count = defaultdict(int), 0
    for letter in string:
        map[letter] += 1
        if(map[letter] > 1 and prevLetter != letter):
            prevLetter = letter
            count += 1
    print("YES" if(count > 1) else "NO")