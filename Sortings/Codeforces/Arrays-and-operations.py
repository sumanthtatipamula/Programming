from math import floor

for _ in range(int(input())):
    n, k = map(int, input().split())
    elements = list(map(int, input().split()))
    elements.sort()
    left, right, score = len(elements) - 2 * k, len(elements) - k, 0
    for _ in range(k):
        score += int(floor(elements[left] / elements[right]))
        left += 1
        right += 1
    print(sum(elements[: len(elements) - 2 * k]) + score)
        
